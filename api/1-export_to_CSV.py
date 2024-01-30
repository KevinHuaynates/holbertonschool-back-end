#!/usr/bin/python3
"""Module to export data to CSV"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]

    user_info_url = (
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(user_id)
    )
    tasks_url = (
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(user_id)
    )
    user_info = requests.get(user_info_url).json()
    username = user_info.get('username')

    tasks = requests.get(tasks_url).json()

    filename = '{}.csv'.format(user_id)

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for task in tasks:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": (
                    "True" if task["completed"]
                    else "False"
                ),
                "TASK_TITLE": task["title"]
            })

    print("Number of tasks in CSV: OK")
