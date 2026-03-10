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

    def get_tasks(self): 
        """
        Used to get all tasks that are active
        """
        sql_get_task = """
            SELECT taskid, title, completed, created_at
            FROM tasks WHERE active = 1
        """
        return self.query(sql_get_task)
        
    def get_status(self, taskid: int) -> int | None:
        """
        Function used to internal get the status of a task
        """
        sql_get_status = "SELECT completed FROM tasks WHERE taskid = ?"
        status = self.query(sql_get_status, (taskid,))
        if len(status) < 1 :
            return None
        return status[0][0]

    def update_status(self, taskid: int) -> bool:
        """
        Function used to update the status of a task
        """
        status = self.get_status(taskid) 
        if status == None: 
            return False
        if status == 1: status = 0
        else: status = 1
        sql_update_status = "UPDATE tasks SET completed = ? WHERE taskid = ?"
        self.query(sql_update_status, (status, taskid))
        return True

    def delete_task(self, taskid: int) -> bool:
        sql_delete_task = "UPDATE tasks SET active = 0 WHERE taskid = ?" 
        self.query(sql_delete_task, (taskid,))
        return True
        
    def day_tasks(self):
        sql_day_tasks = """
            SELECT taskid, title, completed, created_at
            FROM tasks WHERE created_at = ? AND active = 1;
        """
        tasks = self.query(sql_day_tasks, (date,))
        return tasks 

    def show_completed_day(self):
        sql_completed_day = """
            SELECT taskid, title, completed, created_at
            FROM tasks WHERE completed = 1 AND created_at = ? AND active = 1;
        """ 
        tasks = self.query(sql_completed_day, (date,))
        return tasks

    def show_left_day(self):
        sql_left_day = """
            SELECT taskid, title, completed, created_at
            FROM tasks WHERE completed = 0 AND created_at = ? AND active = 1;
        """ 
        tasks = self.query(sql_left_day, (date,))
        return tasks
