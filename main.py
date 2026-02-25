#!/usr/bin/env python3

import argparse
from db import init_db, exec_st, add_task, get_tasks, day_tasks, delete_task, update_status, show_completed_day, show_left_day

def show_tasks(values: tuple) -> None:
    '''
    This function get a tuple a print to a console in orden
    '''
    print("task_id  |  title  |  completed  |  date  ")
    for i in values:
        print(i)

def main():

    # initialize todo.sql
    exec_st(init_db)

        # command features to cli
    parser = argparse.ArgumentParser(
            description = "Tool to handle to do activities.")
    
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

