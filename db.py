import sqlite3

DB_NAME = "todo.sql"

def exec_st(func, **kwargs):
    with sqlite3.connect(DB_NAME) as con:
        return func(con, **kwargs)

def init_db(con):
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        taskid INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed INTEGER NOT NULL DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP 
    );
    """)
    con.commit()
    
def add_task(con, title: str):
    cursor = con.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES(?)",(title,))
    con.commit()

def get_tasks(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()

def get_status(con, taskid: int) -> int | None:
    cursor = con.cursor()
    cursor.execute("SELECT completed FROM tasks WHERE taskid = ?;", (taskid,))
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
    cursor.execute("DELETE FROM tasks WHERE taskid = ?", (taskid,))
    con.commit()
    return taskid


def main():
    exec_st(init_db)
    print(exec_st(delete_task, taskid=13))
    

if __name__ == "__main__":
    main()
