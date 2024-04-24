#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""

import json
import requests

if __name__ == "__main__":

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    todo = {}

    for user in users:
        user_id = user.get('id')
        task_list = []
        for task in tasks:
            task_dict = {}
            task_dict["username"] = user.get('username')
            task_dict["task"] = task.get('title')
            task_dict["completed"] = task.get('completed')
            task_list.append(task_dict)
        todo[user_id] = task_list

    file_name = "todo_all_employees.json"
    with open(file_name, mode='w') as file:
        json.dump(todo, file)
