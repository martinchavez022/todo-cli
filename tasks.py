import sqlite3
from db import DatabaseManager
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')

class TaskManager(DatabaseManager):

    def __init__(self):
        super().__init__()
        self.init_db_tasks() 

    def init_db_tasks(self):
        sql_tasks_table = """
        CREATE TABLE IF NOT EXISTS tasks (
            taskid INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0,
            created_at DATE, 
            active INT DEFAULT 1
        );
        """
        self.query(sql_tasks_table)

    def add_task(self, title: str) -> bool:
        """
        Used to add task 
        """
        sql_add_task = "INSERT INTO tasks (title, created_at) VALUES(?, ?)"
        if self.query(sql_add_task, (title,date)) > 0:
            return True
        return False

    def get_tasks(self) -> bool:
        """
        Used to get all tasks that are active
        """
        sql_get_task = """
            SELECT taskid, title, completed, created_at
            FROM tasks WHERE active = 1
        """
        if self.query(sql_get_task).len() > 0:
            return True
        return False

    def get_status(con, taskid: int) -> int | None:
        cursor = con.cursor()
        cursor.execute("SELECT completed FROM tasks WHERE taskid = ?", (taskid,))
        status = cursor.fetchone()
        return status[0]

    def update_status(con, taskid: int) -> int | None:
        status = exec_st(get_status, taskid=taskid)
        if status == None: 
            return None
        cursor = con.cursor()
        if status == 1: status = 0
        else: status = 1
        cursor.execute("UPDATE tasks SET completed = ? WHERE taskid = ?", (status, taskid))
        con.commit()
        return status

    def delete_task(con, taskid: int) -> int | None:
        cursor = con.cursor()
        cursor.execute("UPDATE tasks SET active = 0 WHERE taskid = ?", (taskid,))
        con.commit()
        return taskid
        
    def day_tasks(con):
        cursor = con.cursor()
        cursor.execute("""
            SELECT taskid, title, completed, created_at
            FROM tasks WHERE created_at = ? AND active = 1;
        """, (date,))
        tasks = cursor.fetchall()
        return tasks

    def show_completed_day(con):
        cursor = con.cursor()
        cursor.execute("""
            SELECT taskid, title, completed, created_at
            FROM tasks WHERE created_at = ? AND active = 1;
        """, (date,))
        tasks = cursor.fetchall()
        return tasks

    def show_completed_day(con):
        cursor = con.cursor()
        cursor.execute("""
            SELECT taskid, title, completed, created_at
            FROM tasks WHERE completed = 1 AND created_at = ? AND active = 1;
        """, (date,))
        tasks = cursor.fetchall()
        return tasks

    def show_left_day(con):
        cursor = con.cursor()
        cursor.execute("""
            SELECT taskid, title, completed, created_at
            FROM tasks WHERE completed = 0 AND created_at = ? AND active = 1;
        """, (date,))
        tasks = cursor.fetchall()
        return tasks
