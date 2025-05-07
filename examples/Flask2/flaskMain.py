from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/pages/<path>')
def page(path):
    print(path)
    return render_template(f"/pages/{path}")

@app.route('/')
def index():
    return render_template(f"../Site/pages/index.html")

if __name__ == '__main__':
    app.run(debug=True)