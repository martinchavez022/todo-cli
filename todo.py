#!/usr/bin/env -S uv run --script

import argparse
from tasks import TaskManager
from pretty_cly import table_data

task_manager = TaskManager()

def main():
    # Main arg parser 
    parser = argparse.ArgumentParser(
            description = "Tool to handle tasks and habits.",
            prog="todo"
    )
    
    # handle tasks vs habits
    subparsers = parser.add_subparsers(dest="module", help="choose a module")

    # task module --------------------------------------------------------
    task_parser = subparsers.add_parser("tasks", help="Manage daily tasks")
    task_sub = task_parser.add_subparsers(dest="action")
    # show tasks 
    show_tasks = task_sub.add_parser("show", help="List of the tasks")
    # add task
    add_task = task_sub.add_parser("add", help="Add a new task")
    add_task.add_argument("tittle", help="Title or description of the task")
    # remove task
    delete_task = task_sub.add_parser("delete", help="Remove a task")
    delete_task.add_argument("taskid", type=int, help="The id of the task to remove")
    # complete
    comple_task = task_sub.add_parser("complete", help="Mark as complete a task")
    comple_task.add_argument("taskid", type=int, help="The id of the task to complete")
    # show-complete
    show_complete = task_sub.add_parser("show-complete", help="Show the completed tasks of the day")
    # show-left
    show_left = task_sub.add_parser("show-left", help="Show left tasks of the day")
    # show-all
    show_all = task_sub.add_parser("show-all", help="Show all tasks")

    # habits module -------------------------------------------------------


    args = parser.parse_args()

    if args.module == "tasks":
        match(args.action):
            case "show":
                table_data(task_manager.day_tasks())
            case "add":
                task_manager.add_task(args.tittle)
            case "delete":
                task_manager.delete_task(args.taskid)
            case "complete":
                task_manager.update_status(args.taskid)
            case "show-complete":
                table_data(task_manager.show_completed_day())
            case "show-left":
                table_data(task_manager.show_left_day())
            case "show-all":
                table_data(task_manager.get_tasks())
            case _:
                print("asd")
    else: 
        return

if __name__ == '__main__':
    main()

