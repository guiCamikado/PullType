import sqlite3
con = sqlite3.connect("database.db")


class SQLFunctions:
    # Função que averigua se um banco de dados existe ou não.
    def tableExists(db_path, table_name):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        result = cur.fetchone()

        conn.close()
        return bool(result)

    def create():
        cur = con.cursor()
        cur.execute("CREATE TABLE TABELA_INTRODUCAO(titulo, autor, data_criacao)")
        cur.execute("CREATE TABLE TABELA_DADOS(id_guia_vinculado, version, mod_name, mod_data, content)")
        cur.close()


    ''' Cria tabela 

    A tabela em questão por hora possui alguns campos sendo eles:

    Tabela-1 Introducao -> Deve possuir Titulo, Autor, Data_Criacao e PrimaryKey.
    A ideia aqui é que esse item seja mostrado na página que mostra todos os guias.

        Cada item da tabela-1 deverá possuir uma tabela própria para versionamento em resumo LOGs esses logs devem conter:

        Tabela-2 DADOS -> PrimaryKey, IdGuiaVinculado, Versão, NomeModificador, DataModificado e Dados.

        A ideia aqui é criar algo como se fosse a wikipedia para caso alguem queira desfazer uma alteração etc...
        '''

    # Conecta-se com banco de dados e retorna nome das colunas
    def getColumnNames(db_path, table_name):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [col[1] for col in cursor.fetchall()]

        conn.close()

        if columns:
            print(f"Columns in '{table_name}': {', '.join(columns)}")
        else:
            print(f"Table '{table_name}' not found!")
    getColumnNames('database.db', 'TABELA_INTRODUCAO')
