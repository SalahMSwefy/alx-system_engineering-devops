#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(user_id)).json()
    user_name = user.get('username')

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(user_id)).json()

    file_name = user_id + ".csv"
    with open(file_name, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in tasks:
            writer.writerow([user_id, user_name, task.get('completed'),
                            task.get('title')])
