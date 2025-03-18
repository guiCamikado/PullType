import sqlite3

class SQLCRUD:
    
    def sql_create(tableName, dbPath, array=[]):
       conn = sqlite3.connect(dbPath)
       cur = conn.cursor()

        values = ""
        
        for element in array:
            if values:
                values += ","
            values += element

       cur.executemany(f"INSERT INTO {tableName} VALUES (?)", [(values,)])

       conn.commit()
       conn.close()

    def sql_read(tableName, dbPath, values, where):
        conn = sqlite3.connect(dbPath)
        cur = conn.cursor()
        cur.execute(f"SELECT {values} FROM {tableName} WHERE {where}")

        return cur.fetchall()

    def sql_update(tableName, dbPath, values, array=[]):
      conn = sqlite3.connect(dbPath)
      cur = conn.cursor()
      
      # Assuming 'array' contains column names and new values
      cur.execute(f"UPDATE {tableName} SET {', '.join([f'{col} = ?' for col, value in zip(values[::2], values[1::2])])} WHERE type='table' AND name='{tableName}'", array)

      conn.commit()
      conn.close()

    def sql_delete(tableName, dbPath, where):
      conn = sqlite3.connect(dbPath)
      cur = conn.cursor()
      
      # Assuming 'array' contains column names and new values
      cur.execute(f"DELETE * FROM {tableName} WHERE PRIMARY_KEY = ?", {(where,)})

      conn.commit()
      conn.close()

# Usage examples:
SQLCRUD.sql_create("my_table", "database.db", ["value1", "value2", "value3"])
SQLCRUD.sql_read("my_table", "database.db", "*", "id > 0")
SQLCRUD.sql_update("my_table", "database.db", ["name", "email"], ["John Doe", "john@example.com"])
SQLCRUD.sql_delete("my_table", "database.db", "0")