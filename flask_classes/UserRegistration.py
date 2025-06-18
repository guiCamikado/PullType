from flask import Blueprint, request, jsonify
import sqlite3

UserRegistration = Blueprint('UserRegistration', __name__)

# Programa inicia aqui recebendo dados do front-end
@UserRegistration.route('/DBAction/sendRegistrationRequest', methods=['POST'])
def sendRegistrationRequest():
    data = request.get_json()  # Recebe os dados enviados em JSON

    # Exemplo de extração dos dados
    usuario = data.get("usuario")
    email = data.get("email")
    nome = data.get("nome")
    sobrenome = data.get("sobrenome")
    senha = data.get("senha")
    confirmar_senha = data.get("confirmarSenha")
    data_nascimento = data.get("dataNascimento")
    termos_aceitos = data.get("termosAceitos")

    # Aqui você adiciona os dados no seu banco de dados SQLite
    # Exemplo fictício:
    # db.insert_usuario(nome, sobrenome, email, senha...)

    # Criar lógica de criar banco de dados se não existir
    # Se existir verificar se usuário ou Email já consta no banco de dados
    # Se usuário não constar no DB inserir usuário e confirmar registro

    return jsonify({"message": "Usuário registrado com sucesso!"}), 200


# Cria banco de dados caso o mesmo não exista ou não seja encontrado
def createTableIfNotExist():
    # WIP especificar o local de criação do banco de dados para database/database
    conexao = sqlite3.connect('database.db')

    # Cria um cursor para executar comandos SQL
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

#WIP essa função deverá checar se usuário ou e-mail já estão ou não registrados no banco de dados e retornar uma booleana com base nisso
def checkValidation():
    return ""

# WIP essa função deverá gerar uma chave de recuperação de senha. A mesma deverá ser executada apenas se a função checkValidation retornar true
def generateRecoveryToken():
    token = ""
    return token

# WIP essa função deve inserir os dados recebidos no banco de dados se todas as validações forem credenciadas.
def insertIntoDataBase():
    return ""