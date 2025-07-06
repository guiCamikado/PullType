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
    
    # Dados
    data = request.get_json()
    databaseCheckup = data.get("login")
    senha = data.get("senha")
    databaseCheckup = checkLogin(databaseCheckup, senha)

    if databaseCheckup:
        #If login is a success
        return jsonify({"success": True}), 200
    else:
        #If login is unsuccessful
        return jsonify({"success": False}), 200


# Confere se usuário ou email existem no banco e se senha está correta retornando um True ou False
def checkLogin(login, senha):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT password FROM TABLE_USERS 
            WHERE username = ? OR email = ?
        """, (login, login))
        
        result = cursor.fetchone()

    if result:
        stored_hash = result[0]
        print(stored_hash)
        print(senha)
        print(bcrypt.checkpw(senha.encode('utf-8'), stored_hash.encode('utf-8')))
        return bcrypt.checkpw(senha.encode('utf-8'), stored_hash.encode('utf-8'))
    else:
        return False