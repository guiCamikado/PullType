# __init__.py
from flask import Flask

#Registra módulos vindos de outras páginas
from flask_classes.Flask_Pages import pages
from flask_classes.UserRegistration import UserRegistration

app = Flask(__name__)
app.register_blueprint(pages)
app.register_blueprint(UserRegistration)

if __name__ == '__main__':
    app.run(debug=True)