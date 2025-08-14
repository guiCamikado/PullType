"""30/06/2025 UserLogin
    Esse código verifica se o usuário e senha digitados no login existem no
    Banco de dados e com base nisso devolve uma resposta.
"""

from flask import Blueprint, request, jsonify, make_response
import sqlite3
import bcrypt
import Flask.PageTools.JWTAuth as JWTAuth

UserLogin = Blueprint('UserLogin', __name__)

#Programa inicia recebendo dados do front

#TESTES

@UserLogin.route('/DBAction/sendLoginRequest', methods=['POST'])
def sendLoginRequest():
    # Dados
    data = request.get_json()
    databaseCheckup = data.get("login")
    senha = data.get("senha")
    rememberMe = data.get("rememberMe", False)

    if checkLogin(databaseCheckup, senha):
        #If login is a success
        databaseCheckup = getUsername(databaseCheckup) # Changes token if email instead of user
        return JWTAuth.generateLoginToken(databaseCheckup, rememberMe)
    
    else:
        #If login is unsuccessful
        return jsonify({"success": False}), 200
    

@UserLogin.route('/DBAction/sendValidationRequest')
def validateToken():
    return JWTAuth.validateToken()

@UserLogin.route('/DBAction/sendLogoutRequest')
def sendLogoutRequest():
    return JWTAuth.logoffToken()

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
        return bcrypt.checkpw(senha.encode('utf-8'), stored_hash.encode('utf-8'))
    else:
        return False
    
def getUsername(login):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT username FROM TABLE_USERS 
            WHERE username = ? OR email = ?
        """, (login, login))
        
        result = cursor.fetchone()

    if result:
        stored_hash = result[0]
        return stored_hash
    else:
        return False