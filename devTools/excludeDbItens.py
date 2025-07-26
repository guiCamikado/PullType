import sqlite3

def deleteUsername(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM TABLE_USERS WHERE username = ?
    ''', (username,))

    conn.commit()
    conn.close()
    print("item deletado")
deleteUsername("guilherme")