# __init__.py
from flask import Flask

#Registra módulos vindos de outras páginas
from flask_classes.Flask_Pages import pages
from flask_classes.UserRegistration import UserRegistration
from flask_classes.UserLogin import UserLogin

app = Flask(__name__, static_folder="static")
app.register_blueprint(pages)
app.register_blueprint(UserRegistration)
app.register_blueprint(UserLogin)

if __name__ == '__main__':
    app.run(debug=False)