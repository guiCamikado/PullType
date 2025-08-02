""" 18/07/25 - Login.py
    'Esse código serve para gerenciar o sistema JWT (Json Web Token) que nada mais é do que uma chave de autentificação para um usuário quando o mesmo se conectar no site.
    
Junto disso esse código serve para:
    - Cria token criptografa o mesmo e o envia para o usuário
    - Verificar se o token é valido quando usuário desejar requisição.
    - Excluir o token caso requisitado pelo usuário.
"""

from flask import Flask, request, make_response, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "Definir uma chave secreta aqui!"

# Cria Token
def generateLoginToken(username: str, rememberMe: bool):
    print(type(rememberMe))
    token = jwt.encode(
        {
        'user': username,
        'exp': datetime.datetime.now() + datetime.timedelta(hours= 24 * 7),
        },
        app.config['SECRET_KEY'],
        algorithm='HS256'
    )

    response = make_response({"success": True})
    if rememberMe == "true":
        response.set_cookie('pullType_acess_token',
                            token,
                            httponly=True,
                            secure=True,
                            samesite='Lax',
                            max_age= 24 * 60 * 60 * 21)
    else:
        response.set_cookie('pullType_acess_token',
                            token,
                            httponly=True,
                            secure=True,
                            samesite='Lax')
    return response

# Valida Token
def validateToken():
    data = request.cookies.get('pullType_acess_token')
    if not data:
        print("Not data")
        return jsonify({"message": "Error, Verify validateToken in 'UserAuth.py'"})

    try:
        token = jwt.decode(
            data, app.config['SECRET_KEY'], algorithms=["HS256"]
        )
        return token
    except:
        # Se a chave JWT for modificada seja por qualquer motivo como uma tentativa de falsificar a chave isso aparecer-irá
        return jsonify({"message":"the cookie 'pullType_acess_token' was modiffied and cannot be decoded because of this for more info see on UserAuth.py"})
        
# Valida token e retorna usuário
def returnUser():
    data = request.cookies.get('pullType_acess_token')
    if not data:
        print("Not data")
        return jsonify({"message": "Error, Verify validateToken in 'UserAuth.py'"})

    try:
        token = jwt.decode(
            data, app.config['SECRET_KEY'], algorithms=["HS256"]
        )
        user = token.get("user")
        return user
    except:
        # Se a chave JWT for modificada seja por qualquer motivo como uma tentativa de falsificar a chave isso aparecer-irá
        return jsonify({"message":"the cookie 'pullType_acess_token' was modiffied and cannot be decoded because of this for more info see on UserAuth.py"})
    

# Exclui token caso requisitado pelo usuário
def logoffToken():
    response = make_response(jsonify({"message": "User logged out"}))
    response.delete_cookie('pullType_acess_token')  # this handles all options like max_age, etc.
    return response