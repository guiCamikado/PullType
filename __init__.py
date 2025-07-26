# __init__.py
from flask import Flask
app = Flask(__name__, static_folder="static")

#Registra módulos vindos de outras páginas
from Flask.Flask_Pages import pages
app.register_blueprint(pages)

from Flask.UserRegistration import UserRegistration
app.register_blueprint(UserRegistration)

from Flask.UserLogin import UserLogin
app.register_blueprint(UserLogin)

from Flask.verifyToken import verifyToken
app.register_blueprint(verifyToken)


if __name__ == '__main__':
    app.run(debug=True)