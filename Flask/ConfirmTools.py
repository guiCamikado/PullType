import sqlite3
def verifyEmail(key):
    print(key)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT username FROM TABLE_USERS
        WHERE email_confirmed = ?
    """, (key,))

    result = cursor.fetchone()

    if result:
        cursor.execute("""
            UPDATE TABLE_USERS
            SET email_confirmed = ?
            WHERE username = ?
        """, (True, result[0]))

        conn.commit()
    conn.close()

    if result:
        return True
    else:
        return False