""" flask_pages.py _ Ultima modificação: 14/07/2025
Esta página serve para gerar URLs acessiveis ao usuário e pela
 própria aplicação Flask
"""
import os
from flask import Blueprint, render_template, send_from_directory, abort
import json

pages = Blueprint('flask_pages', __name__)

# Homepage
@pages.route('/') 
def index():
    return render_template('pages/home.html')

# Favicon do site
@pages.route('/favicon.ico') 
def favicon():
    return send_from_directory('static', 'favicon.ico')

# Qualquer imagem dentro da static
@pages.route("/images/<path:path>") 
def getImages(path):
    return render_template(f"static/images/{path}")

# Layouts padrão do site quando Offline
@pages.route("/layouts/topMenu/<path:path>") 
def server_menu_css(path):
    return render_template(f"templates/layouts/topMenu/{path}")

# Layout padrão do site quando online (WIP)
@pages.route("/templates/layouts/topMenuConnected/<path:path>") 
def server_menu_js_connected(path):
    return render_template(f"templates/layouts/topMenu/{path}")

# Procura de perfis (WIP)
# Está faltando a possibilidade de edição
# Está faltando a possibilidade de enviar informações como Bio para o front
# 
@pages.route("/profile/<username>")
def profile(username):

    print(os.getcwd())
    profile_path = os.path.join('static', 'users', username, 'profile', 'profile.json')
    try:
        with open(profile_path, 'r', encoding='utf-8') as f:
            profile_data = json.load(f)
    except FileNotFoundError:
        return f"User profile '{username}' not found.", 404
    except json.JSONDecodeError:
        return f"Invalid JSON for user '{username}'.", 500

    itensToSend = {
        'profilePicture': f'users/{username}/image/profilePicture.png',
        'profile_data': profile_data
    }
    return render_template('pages/profile.html', **itensToSend)

# Qualquer caminho aberto dentro da "pages"
@pages.route('/<path:path>') 
def anyPageInsidePages(path):
    return render_template(f'pages/{path}.html')