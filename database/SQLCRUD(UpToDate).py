from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE_NAME = 'database.db'

@app.route('/api/useSql', methods=["POST"])
def useSQLiteCrud():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    sqlAction = data.get('action')
    if sqlAction not in ['insert', 'read', 'update', 'delete']:
        return jsonify({"error": "Invalid action"}), 400
    
    # Prepare SQL query parameters
    params = {
        'table': data.get('tableName'),
        'where': data.get('where'),
        'data': data.get('data')
    }
    
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cur = conn.cursor()
        
        if sqlAction == 'insert':
            placeholders = ', '.join(['?' for _ in range(len(params['data']))])
            sql = f"INSERT INTO {params['table']} VALUES ({placeholders})"
            cur.executemany(sql, params['data'])
            conn.commit()
            return jsonify({"message": "Record inserted successfully"}), 201
        
        elif sqlAction == 'read':
            sql = f"SELECT * FROM {params['table']}"
            if params['where']:
                sql += f" WHERE {params['where']}"
            cur.execute(sql)
            
            result = cur.fetchall()
            return jsonify({"result": result}), 200
        
        elif sqlAction == 'update':
            placeholders = ', '.join(['?' for _ in range(len(params['data'][0]))])
            sql = f"UPDATE {params['table']} SET {', '.join([f'{key}=?' for key in params['data'][0]])} WHERE {params['where']}"
            cur.execute(sql, [item for sublist in params['data'] for item in sublist] + [True])
            conn.commit()
            return jsonify({"message": "Record updated successfully"}), 200
        
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
        "action": "insert",
        "where": "",
        "data": [["nome", "email"], ["John Doe", "john@example.com"]]
    }
    response = useSQLiteCrud(data)
    return jsonify({"result": response})

# 2. Read records
@app.route('/api/example-read')
def example_read():
    data = {
        "action": "read",
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