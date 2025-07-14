# __init__.py
from flask import Flask
app = Flask(__name__, static_folder="static")

#Registra módulos vindos de outras páginas
from flask_classes.Flask_Pages import pages
app.register_blueprint(pages)

from flask_classes.UserRegistration import UserRegistration
app.register_blueprint(UserRegistration)

from flask_classes.UserLogin import UserLogin
app.register_blueprint(UserLogin)

from flask_classes.verifyToken import verifyToken
app.register_blueprint(verifyToken)


if __name__ == '__main__':
    app.run(debug=True)