""" flask_pages.py _ Ultima modificação: 14/07/2025
Esta página serve para gerar URLs acessiveis ao usuário pela
 própria aplicação Flask aqui se tem links
"""
import os
from flask import Blueprint, render_template, send_from_directory, abort, request, jsonify
from Flask import JWTAuth as JWTAuth
import topMenuTools as topMenuTools
import json

pages = Blueprint('flask_pages', __name__)

# Homepage
# @pages.route('/')
# def goToHomepage():
#     return goToAnypage(path = "")

# Confirmação de e-mail
@pages.route('/confirm/<path:key>')
def goToConfirm(key):
    from Flask import ConfirmTools
    result = ConfirmTools.verifyEmail(key)
    if result:
        send = {
            "message": """
                <p><strong>Seu e-mail foi confirmado com sucesso!</strong></p>
                <p>Você já pode fechar esta aba e acessar todos os recursos disponíveis na plataforma.</p>
            """
        }
        return render_template('pages/verify.html', **send)
    else:
        send = {
            "message": """
                <p><strong>Algo deu errado!</strong></p>
                <p>O link pode não ser mais válido. Você pode fechar esta aba e tentar criar uma conta novamente.</p>
                <p>Se o problema persistir, entre em contato com nossa equipe de suporte.</p>
            """
        }
        return render_template('pages/verify.html', **send)

# Vai para qualquer página
@pages.route('/')
@pages.route('/<path:path>') 
def goToAnypage(path = ""):
    checkLogin = request.cookies.get('pullType_acess_token') #Confere se usuário está ou não conectado
    if checkLogin:
        if(path == ""):
            return render_template(f'pages/home.html')
        return render_template(f'pages/{path}.html')
    elif (path == "" or path =="/"):
        return render_template('pages/login.html')
    else:
        return render_template(f'pages/{path}.html')

# Favicon do site
@pages.route('/favicon.ico') 
def getFavicon():
    return send_from_directory('static', 'favicon.ico')

# Qualquer imagem dentro da static
@pages.route("/images/<path:path>") 
def getImages(path):
    return render_template(f"static/images/{path}")

@pages.route("/profile/<username>")
def goToProfile(username):
    profile_path = os.path.join('static', 'users', username, 'profile', 'profile.json')
    loginCookie = JWTAuth.returnUser()
    print(loginCookie)
    print(loginCookie)
    print(loginCookie)
    print(loginCookie)
    botaoDeSeguirOuEditar = "<button>Seguir</button>"
    if username == loginCookie:
        botaoDeSeguirOuEditar = "<button onclick='goToProfileEditor()'>Editar</button>"
    try:
        with open(profile_path, 'r', encoding='utf-8') as file:
            profile_data = json.load(file)
    except FileNotFoundError:
        return f"User profile '{username}' not found.", 404
    except json.JSONDecodeError:
        return f"Invalid JSON for user '{username}'.", 500

    itensToSend = {
        'profilePicture': f'users/{username}/image/profilePicture.png', #Tratar isso para aceitar tanto png, jpeg, jpg e gif
        'profile_data': profile_data,
        'botaoDeSeguirOuEditar': botaoDeSeguirOuEditar
    }
    return render_template('pages/profile.html', **itensToSend)

# WIP Vai para a página de edição de perfil
@pages.route('/profile/edit')
def goToProfileEdition():
    checklogin = JWTAuth.returnUser()

    profileItens = {
        'username': checklogin
    }

    return render_template(f"pages/profileEdit.html", **profileItens )


# Envia arquivos utilizados em todas as páginas
@pages.context_processor
def sendUserAssets():
    try:
        profilePicture = topMenuTools.getUserProfilePicture()
        user = JWTAuth.returnUser()
    except:
        return {}
    # Retorna para uso nos templates
    return dict(userAssets={
        'profilePicture': profilePicture,
        'username': user
        })