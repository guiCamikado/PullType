# flask_pages.py
from flask import Blueprint, render_template, send_from_directory

pages = Blueprint('flask_pages', __name__)

@pages.route('/')
def index():
    return render_template('pages/index.html')

@pages.route('/<path:path>')
def anyPageInsidePages(path):
    return send_from_directory('templates/pages', path)

@pages.route("/images/<path:path>")
def getImages(path):
    return send_from_directory("static/images", path)

@pages.route("/templates/layouts/topMenu/<path:path>")
def server_menu_js(path):
    return send_from_directory("templates/layouts/topMenu", path)

@pages.route("/templates/layouts/topMenu/<path:path>")
def server_menu_html(path):
    return send_from_directory("templates/layouts/topMenu", path)

@pages.route("/layouts/topMenu/<path:path>")
def server_menu_css(path):
    return send_from_directory("templates/layouts/topMenu", path)