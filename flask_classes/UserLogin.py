"""30/06/2025 UserLogin
    Esse código verifica se o usuário e senha digitados no login existem no
    Banco de dados e com base nisso devolve uma resposta.
"""

from flask import Blueprint, request, jsonify
import sqlite3
import bcrypt

UserLogin = Blueprint('UserLogin', __name__)

#Programa inicia recebendo dados do front

#TESTES

@UserLogin.route('/DBAction/sendLoginRequest', methods=['POST'])
def sendLoginRequest():
    # data = request.get_json()
    # Dados
    # login = data.get("login")
    # senha = data.get("senha")

    # Teste
    login = "teste"
    senha = "teste"

    checkLogin(login, senha)


# Confere se usuário ou email existem no banco e se senha está correta retornando um True ou False
def checkLogin(login, senha):

    loginConfirmation = False
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    password = senha.encode('utf-8')
    password = bcrypt.hashpw(password, bcrypt.gensalt())
    print(password)

    cursor.execute("""
    SELECT COUNT(*) FROM TABLE_USERS WHERE 
                username = ? OR
                email = ? AND
                password = ?
""", (login, login, password,))
    
    result = cursor.fetchone()

    if result[0] > 0:
        loginConfirmation = True

    conn.close()
    return loginConfirmation


sendLoginRequest()