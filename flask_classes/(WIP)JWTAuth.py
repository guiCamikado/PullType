''' 30/06/2025 JWTAuth
    Esse código gera um JWT (Json Web Token) que será utilizada para AUTORIZAÇÃO de usuários já autenticados(vale lembrar que o payload não é criptografado apesar de que nada será necessáriamente enviado.)
'''

import jwt
import datetime
key = "v#7Pq@Lz!fT9r*Wd"
payload = {}

def sendJWT():
    encoded = jwt.encode

encoded = jwt.encode(payload,
                     key,
                     algorithm="HS256")
print(encoded)

decoded = jwt.decode(encoded,
                     key,
                     algorithms="HS256")

teste = jwt.encode
print(decoded)

def generateLoginToken(username:str, rememberMe: bool):
    token = jwt.encode({
        'user': username,
        'exp': datetime.datetime.now() + datetime.timedelta(hours= 24 * 7),
    },)

    response = make_response({"message":"apenasTestando"})
    if rememberMe:
        response.set_cookie('acess_token',
                            token,
                            httponly=True,
                            secure=True,
                            samesite='Lax',
                            max_age= 24 * 60 * 60 * 365)
    else:
        response.set_cookie('acess_token',
                            token,
                            httponly=True,
                            secure=True,
                            samesite='Lax')
    return response