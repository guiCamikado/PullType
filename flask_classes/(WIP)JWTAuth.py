''' 30/06/2025 JWTAuth
    Esse código gera um JWT (Json Web Token) que será utilizada para AUTORIZAÇÃO de usuários já autenticados(vale lembrar que o payload não é criptografado apesar de que nada será necessáriamente enviado.)
'''

import jwt
key = "senha_12dwadawd3"
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