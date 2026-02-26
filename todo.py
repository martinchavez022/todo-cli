#!/usr/bin/env -S uv run --script

import argparse
from rich.console import Console
from rich.table import Table
from rich import box
from db import init_db, exec_st, add_task, get_tasks, day_tasks, delete_task, update_status, show_completed_day, show_left_day

console = Console()

def show_tasks(values: tuple) -> None:
    table = Table(title="TASKS", box=box.HORIZONTALS)

    table.add_column("TASKID", justify="center")
    table.add_column("TASK", style="bold royal_blue1")
    table.add_column("COMPLETED", justify="center")
    table.add_column("DATE", justify="center")

    for taskid, title, completed, created_at in values:
        table.add_row(str(taskid), title, str(completed), created_at) 
    console.print(table)

def main():

    # initialize todo.sql
    exec_st(init_db)

        # command features to cli
    parser = argparse.ArgumentParser(
            description = "Tool to handle 'to do' activities.",
            epilog = """
features avialable:
    - add
    - show
    - show-all
    - show-completed
    - show-left
    - completed
    - delete
    """,
            formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # the only characteristic that is neccesary
    parser.add_argument("feature", help="Indicates the action to do")
    
    # values to do the feature
    parser.add_argument("--title", help="The title to new task")
    parser.add_argument("--taskid", help="The task id of the task")

    args = parser.parse_args()

    match(args.feature):
        case "add":
            if not args.title:
                raise Exception("The title value is necessary to this feature")
            exec_st(add_task, title=args.title) # insert new task
            return

        case "show-all":
            show_tasks(exec_st(get_tasks))
            return
        
        case "show":
            show_tasks(exec_st(day_tasks))
            return

        case "show-completed":
            show_tasks(exec_st(show_completed_day))
            return

        case "show-left":
            show_tasks(exec_st(show_left_day))
            return

        case "delete":
            if not args.taskid:
                raise Exception("The taskid value is necessary to this feature")
            if exec_st(delete_task, taskid=args.taskid) != None:
                return    
            raise Exception("The task was not deleted")
        
        case "completed":
            if not args.taskid:
                raise Exception("The taskid value is neccessary to this feature")
            if exec_st(update_status, taskid=args.taskid) != None:
                return
            raise Exception("The task was not mark as completed")

        case _:
            raise Exception("Invalid command.")

if __name__ == '__main__':
    main()

