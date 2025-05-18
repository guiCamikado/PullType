import sqlite3

# Conecta (ou cria) o banco de dados
conexao = sqlite3.connect('database.db')

# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

# Cria a tabela "usuarios"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS TABLE_USERS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    password TEXT NOT NULL,
    user_born_in DATE NOT NULL,
    recovery_key TEXT,
    account_created DATE,
    last_section DATE,
    google_oAuth BOOL,
    receive_email BOOL,
    email_confirmed BOOL)
''')

# Salva (commit) as alterações
conexao.commit()

# Fecha a conexão
conexao.close()