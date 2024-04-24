#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(user_id))
    user_name = user.json().get('name')

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(user_id))
    tasks = tasks.json()

    completed_tasks = [task for task in tasks if task.get('completed') is True]

    print("Employee {} is done with tasks({}/{}):".
          format(user_name, len(completed_tasks), len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
