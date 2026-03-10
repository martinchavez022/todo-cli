import sqlite3

class DatabaseManager:
    def __init__(self): 
        self.db_name = "todo.sql"
    
    def query(self, sql, params=()):
        """
        This function works as global execute query of any type
        """
        with sqlite3.connect(self.db_name) as con:
            cursor = con.cursor()
            cursor.execute(sql, params)
            con.commit()
            
            if sql.strip().upper().startswith("SELECT"):
                return cursor.fetchall()

            return cursor.lastrowid


