""" 15/07/2025 ProfileTools
    Essa página serve para obter e escrever informações da pasta users para a pagina "profile.html" quando a mesma for carregada. Ela é uma extensão da
    função profile() em Flask_Pages.
"""

from flask import Blueprint, jsonify, render_template, send_from_directory
import os

app = Blueprint("ProfileTools", __name__)

class ProfileTools(username):
    pointer = os.chdir(f'users/{username}')