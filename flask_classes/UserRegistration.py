from flask import Blueprint, request, jsonify
import sqlite3

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
        print("if1")
        if checkEmailValidation(email):
            insertIntoDataBase(usuario, email, nome, sobrenome, senha, data_nascimento, token)
            print ("If2")
            return jsonify({"message": "Usuário registrado com sucesso!"}), 200
        
        else:
            print("if3")
            return jsonify({"message":"Email já registrado!"}), 200
    else:
        print("if4")
        return jsonify({"message":"Usuário já registrado!"}), 200



# (WIP) Cria banco de dados caso o mesmo não exista ou não seja encontrado
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
    token = ''.join(secrets.choice(alfabeto) for _ in range(16))
    return token

# WIP essa função deve inserir os dados recebidos no banco de dados se todas as validações forem credenciadas.
def insertIntoDataBase(usuario, email, nome, sobrenome, senha, data_nascimento, token):
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
    """, (usuario, email, nome, sobrenome, senha, data_nascimento, token,))

    conn.commit()
    conn.close()