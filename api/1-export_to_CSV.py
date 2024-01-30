#!/usr/bin/python3
"""
Script to export user tasks data in CSV format.

Requirements:
- Records all tasks that are owned by this user.
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} USER_ID".format(argv[0]))
        exit(1)

    user_id = argv[1]
    user_info_url = (
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(user_id)
    )
    tasks_url = (
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(user_id)
    )
    user_response = requests.get(user_info_url)
    tasks_response = requests.get(tasks_url)

    if user_response.status_code != 200:
        print("User not found")
        exit(1)

    user_data = user_response.json()
    tasks_data = tasks_response.json()

    username = user_data.get('username', 'Unknown')
    filename = '{}.csv'.format(user_id)

    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = [
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks_data:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": (
                    "True" if task["completed"]
                    else "False"
                ),
                "TASK_TITLE": task["title"]
            })

    print("CSV file '{}' created.".format(filename))
