""" 08/07/2025
Esse código é utilizado pela página verify.html para verificar o e-mail.

"""
from flask import Blueprint, request, jsonify
import sqlite3
verifyToken = Blueprint('verifyToken', __name__)


    
@verifyToken.route('/DBAction/sendVerificationRequest', methods=['POST'])
def verify():
    # Dados
    data = request.get_json()
    email = data.get("email")
    user = data.get("user")
    key = data.get("key")

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    try:
        cur.execute("SELECT recovery_key FROM TABLE_USERS WHERE email = ? AND username = ?", (email, user))
        result = cur.fetchone()
        if result[0] == key:
            insertTrueVerificationIntoDatabase(email, user)
            return True
        else:
            print("false")
            return False
    finally:
        conn.close()

def insertTrueVerificationIntoDatabase(email, user):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("UPDATE TABLE_USERS SET email_confirmed = ? WHERE email = ? AND username = ?", (True, email, user))

    conn.commit()
    conn.close()