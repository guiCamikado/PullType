from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)

# Ativa modo debug (desativar em ambiente)
if __name__ == '__main__':
    app.run(debug=True, port=5000)

# Prepara dados que chegam
CORS(app, resources={r"/*": {"origins": "*", 
                             "allow_headers": ["Content-Type", "Authorization"],
                             "expose_headers": ["Content-Type", "X-Content-Type-options", "X-Custom-Header"],
                             "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]}})


DATABASE_NAME = 'database.db'

# Realiza a conexão do front com o Back por meio de um link /api/useSql
# Essa conexão é perigosa visto que deixa aberta a edição por parte do user a qualquer tabela do banco de dados. Não utilizar!!!
@app.route('/api/useSql', methods=['GET', 'POST'])
def useSQLiteCrud():

    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    sqlAction = data.get('action')
    if sqlAction not in ['insert', 'select', 'update', 'delete']:
        return jsonify({"error": "Invalid action"}), 400
    
    params = {
        'table': data.get('tableName'),
        'where': data.get('where'),
        'data': data.get('data')
    }
    
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        
        # INSERT
        if sqlAction == 'insert':
            placeholders = ', '.join(['?' for _ in range(len(params['data']))])
            sql = f"INSERT INTO {params['table']} VALUES ({placeholders})"
            cur.executemany(sql, params['data'])
            conn.commit()
            return jsonify({"message": "Record inserted successfully"}), 201
        
        # SELECT
        elif sqlAction == 'select':
            sql = f"SELECT * FROM {params['table']}"
            if params['where']:
                sql += f" WHERE {params['where']}"
            cur.execute(sql)
            
            result = cur.fetchall()
            return jsonify({"result": result}), 200
        
        # UPDATE
        elif sqlAction == 'update':
            placeholders = ', '.join(['?' for _ in range(len(params['data'][0]))])
            sql = f"UPDATE {params['table']} SET {', '.join([f'{key}=?' for key in params['data'][0]])} WHERE {params['where']}"
            cur.execute(sql, [item for sublist in params['data'] for item in sublist] + [True])
            conn.commit()
            return jsonify({"message": "Record updated successfully"}), 200
        
        # DELETE
        elif sqlAction == 'delete':
            sql = f"DELETE FROM {params['table']}"
            if params['where']:
                sql += f" WHERE {params['where']}"
            cur.execute(sql)
            conn.commit()
            return jsonify({"message": "Record deleted successfully"}), 200
    
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)





# Exemplo de Uso:
# 1. Insert a record
@app.route('/api/example-insert')
def example_insert():
    data = {
        "tablename": "TABELA_CONTAS",
        "action": "insert",
        "where": "",
        "data": [["user", "email"], ["John Doe", "john@example.com"]]
    }
    response = useSQLiteCrud(data)
    return jsonify({"result": response})

# 2. Read records
@app.route('/api/example-read')
def example_read():
    data = {
        "action": "select",
        "where": ""
    }
    response = useSQLiteCrud(data)
    return jsonify({"result": response})

# 3. Update a record
@app.route('/api/example-update')
def example_update():
    data = {
        "action": "update",
        "where": "nome=John Doe",
        "data": [["email", "new_email@example.com"]]
    }
    response = useSQLiteCrud(data)
    return jsonify({"result": response})

# 4. Delete a record
@app.route('/api/example-delete')
def example_delete():
    data = {
        "action": "delete",
        "where": "nome=John Doe"
    }
    response = useSQLiteCrud(data)
    return jsonify({"result": response})