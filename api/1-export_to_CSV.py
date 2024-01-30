#!/usr/bin/python3
"""
Extend your Python script to export data in CSV format.
"""
import csv
import requests
from sys import argv


def export_to_csv(user_id):
    api_url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{api_url}/users/{user_id}").json()
    todo_data = requests.get(f"{api_url}/todos?userId={user_id}").json()

    if not users or not todo_data:
        print("User or tasks not found.")
        exit(1)

    username = users["username"]
    filename = f"{user_id}.csv"

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for task in todo_data:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": str(task["completed"]),
                "TASK_TITLE": task["title"]
            })

    print(f"CSV file '{filename}' created.")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <user_id>".format(argv[0]))
        exit(1)

    user_id = argv[1]
    export_to_csv(user_id)
