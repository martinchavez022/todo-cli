#!/usr/bin/env python3

import argparse
from db import init_db, exec_st, add_task, get_tasks, day_tasks 

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
    parser.add_argument("feature", help="indicates the action to do")
    
    # values to do the feature
    parser.add_argument("--title", help="the title to new task")
    
    args = parser.parse_args()

    match(args.feature):
        case "add":
            if not args.title:
                raise Exception("The title value is necessary to this feature")
            exec_st(add_task, title=args.title) # insert new task
            return
        case "showall":
            show_tasks(exec_st(get_tasks))
            return
        case "showday":
            show_tasks(exec_st(day_tasks))
            return
        case _:
            raise Exception("Invalid command.")

if __name__ == '__main__':
    main()

