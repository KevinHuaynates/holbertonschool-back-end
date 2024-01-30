#!/usr/bin/env python3
"""
Export data to CSV format
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) != 2 or not argv[1].isdigit():
        exit()

    user_id = int(argv[1])
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        exit()

    user = user_response.json()
    todos = todos_response.json()

    username = user.get('username')

    if not username:
        exit()

    filename = f'{user_id}.csv'
    fieldnames = [
        "USER_ID",
        "USERNAME",
        "TASK_COMPLETED_STATUS",
        "TASK_TITLE"
    ]

    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for task in todos:
            completed_status = "True" if task["completed"] else "False"

            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": completed_status,
                "TASK_TITLE": task["title"]
            })
