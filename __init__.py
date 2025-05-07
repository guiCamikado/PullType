from flask import Flask, request
import os

from flask import request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return print("Teste")
    else:
        return print("Teste_2")