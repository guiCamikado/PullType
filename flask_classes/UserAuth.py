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

    token = jwt.encode(
        {
        'user': username,
        'exp': datetime.datetime.now() + datetime.timedelta(hours= 24 * 7),
        },
        app.config['SECRET_KEY'],
        algorithm='HS256'
    )

    response = make_response({"message":"Cookie send"})
    if rememberMe:
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

    data = request.get_json()
    if not data:
        return jsonify({"message": "Error, Verify validateToken in 'UserAuth.py' "})
    

    token = jwt.decode(
        data, app.config('SECRET_KEY'), algorithms=["RS256"]
    )


# Exclui token caso requisitado pelo usuário
def LogoffToken():

    #First JSON
    data = request.get_json()
    username = data.get("username")

    token = jwt.encode(
        {'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
        app.config['SECRET_KEY'],
        algorithm='HS256'
    )

    response = make_response()
    response.set_cookie('pullType_acess_token',
                            token,
                            httponly=True,
                            secure=True,
                            samesite='Lax',
                            max_age = 0)
    return response