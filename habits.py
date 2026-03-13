import sqlite3
from db import DatabaseManager
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')

class HabitManager(DatabaseManager):

    def __init__(self):
        super().__init__()
        self.init_db_habits()
    
    """
    database construction
    habits (table)
        This table going to save a list of the list habits

    """
    def init_db_habits(self):
        sql_table_habits = """
        CREATE TABLE IF NOT EXISTS habits(
            habitid INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            created_at DATE NOT NULL,
            active INTEGER DEFAULT 1
        );
        """
        self.query(sql_table_habits)
        sql_table_habit_log = """
        CREATE TABLE IF NOT EXISTS habit_log (
            habitlogid INTEGER PRIMARY KEY AUTOINCREMENT,
            habitid INTEGER,
            date DATE,
            CONSTRAINT fk_habit
            FOREIGN KEY (habitid) REFERENCES habits(habitid),
            UNIQUE (habitid, date)
        );
        """
        self.query(sql_table_habit_log)

    def get_habits(self):
        sql_get_habits = """
            SELECT habitid, title, created_at
            FROM habits;
        """
        return self.query(sql_get_habits)

    def add_habit(self, title: str):
        sql_add_habit = """
            INSERT INTO habits (title, created_at) 
            VALUES (?,?);
        """
        row = self.query(sql_add_habit, (title, date))
        return row

        


    
