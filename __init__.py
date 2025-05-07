from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pages/index.html')  # Render the HTML file from templates/pages

## Pages
@app.route('/pages/<path:path>')
def anyPageInsidePages(path):
    return send_from_directory('templates/pages', path)

## templates/layouts/topMenu
@app.route('/templates/layouts/topMenu/menu.js')
def server_menu_js():
    return send_from_directory("templates/layouts/topMenu", "menu.js")
@app.route('/templates/layouts/topMenu/TopMenu.html')
def server_menu_html():
    return send_from_directory("templates/layouts/topMenu", "TopMenu.html")
@app.route('/layouts/topMenu/topNavegationBar.css')
def server_menu_css():
    return send_from_directory("templates/layouts/topMenu", "topNavegationBar.css")

# Impostores, dar um checkup e expulsar eles da nave
@app.route('/pages/layouts/topMenu/topNavegationBar.css')
def serve_menu_pages_css():
    return send_from_directory("/pages/templates/layouts/topMenu", "topNavegationBar.css")

@app.route('/pages/layouts/topMenu/topMenu.html')
def serve_menu_pages_html():
    return send_from_directory("/pages/templates/layouts/topMenu", "topMenu.html")

if __name__ == '__main__':
    app.run(debug=True)