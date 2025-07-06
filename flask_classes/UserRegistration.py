''' Esse código recebe dados da página de registro para registrar um novo usuário, junto disso ele verifica se o usuário ou e-mail já
    existem na base de dados antes de fazer a inserção'''

from flask import Blueprint, request, jsonify
import sqlite3
import os
import bcrypt

UserRegistration = Blueprint('UserRegistration', __name__)

# Programa inicia aqui recebendo dados do front-end
@UserRegistration.route('/DBAction/sendRegistrationRequest', methods=['POST'])
def sendRegistrationRequest():
    data = request.get_json()  # Recebe os dados enviados em JSON

    # Dados
    usuario = data.get("usuario")
    email = data.get("email")
    nome = data.get("nome")
    sobrenome = data.get("sobrenome")
    senha = data.get("senha")
    confirmar_senha = data.get("confirmarSenha")
    data_nascimento = data.get("dataNascimento")
    termos_aceitos = data.get("termosAceitos")
    token = generateRecoveryToken()

    if senha != confirmar_senha:
        return jsonify({"message": "Senhas não coincidem!"}), 200

    createTableIfNotExist()
    if checkUserValidation(usuario):
        if checkEmailValidation(email):
            insertIntoDataBase(usuario, email, nome, sobrenome, senha, data_nascimento, token)
            generateUserPaste(usuario)
            return jsonify({"message": "Usuário registrado com sucesso!"}), 200
        
        else:
            return jsonify({"message":"Email já registrado!"}), 200
    else:
        return jsonify({"message":"Usuário já registrado!"}), 200



# Cria banco de dados caso o mesmo não exista ou não seja encontrado
def createTableIfNotExist():
    # WIP especificar o local de criação do banco de dados para database/database
    conexao = sqlite3.connect('database.db')
    cursor = conexao.cursor()
    # Cria a tabela "TABLE_USERS" que faz referencias aos usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TABLE_USERS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        password TEXT NOT NULL,
        user_born_in DATE NOT NULL,
        recovery_key TEXT,
        account_created DATE,
        last_section DATE,
        google_oAuth BOOL,
        receive_email BOOL,
        email_confirmed BOOL)
    ''')

    conexao.commit() # Salva (commit) as alterações
    conexao.close() # Fecha a conexão
# Conferem se usuário ou e-mail existem no banco de dados
def checkUserValidation(username):
    existsInDataBase = True

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM TABLE_USERS WHERE username = ?", (username,))

    result = cursor.fetchone()
    
    if result[0] > 0:
        existsInDataBase = False
    
    connection.close()
    return existsInDataBase
def checkEmailValidation(email):
    existsInDataBase = True

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM TABLE_USERS WHERE email = ?", (email,))
    result = cursor.fetchone()
    
    if result[0] > 0:
        existsInDataBase = False
    
    connection.close()
    return existsInDataBase

# WIP essa função deverá gerar uma chave de recuperação de senha. A mesma deverá ser executada apenas se a função checkValidation retornar true
def generateRecoveryToken():

    import secrets
    import string

    alfabeto = string.ascii_letters + string.digits # Letras e Num
    token = ''.join(secrets.choice(alfabeto) for _ in range(5))
    return token

# WIP essa função deve inserir os dados recebidos no banco de dados se todas as validações forem credenciadas.
def insertIntoDataBase(user, email, nome, sobrenome, senha, data_nascimento, token):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO TABLE_USERS (
            username,
            email,
            name,
            last_name,
            password,
            user_born_in,
            recovery_key
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (  user,
            email,
            nome,
            sobrenome,
            returnHash(senha),
            data_nascimento,
            token,))

    conn.commit()
    conn.close()
# Retorna Hash com base no algoritmo de Niels Provos e David Mazières
def returnHash(password):
    password = password.encode('utf-8')
    password = bcrypt.hashpw(password, bcrypt.gensalt())
    return password.decode('utf-8')

# Gera pastas base do user
def generateUserPaste(user):
    users_dir = os.path.join(os.getcwd(), "users")
    os.makedirs(users_dir, exist_ok=True)
    
    full_path = os.path.join(users_dir, user)
    os.makedirs(full_path, exist_ok=True)
    
    image_dir = os.path.join(full_path, "image")
    os.makedirs(image_dir, exist_ok=True)
    
    guides_dir = os.path.join(full_path, "guides")
    os.makedirs(guides_dir, exist_ok=True)