#!/usr/bin/python3
"""
Export employee TODO list progress to CSV format
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])
    api_url = "https://jsonplaceholder.typicode.com"

    # Get user data
    user_response = requests.get("{}/users/{}".format(api_url, employee_id))
    user_data = user_response.json()
    user_id = user_data.get("id")
    user_name = user_data.get("username")

    # Get TODO list
    todo_response = requests.get(
        "{}/todos?userId={}".format(api_url, employee_id)
    )
    todo_data = todo_response.json()

    # Filter tasks owned by the user
    user_tasks = [task for task in todo_data if task['userId'] == employee_id]

    # Export to CSV
    csv_file_name = "{}.csv".format(user_id)
    with open(csv_file_name, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in user_tasks:
            csv_writer.writerow([
                user_id,
                user_name,
                str(task.get("completed")),
                task.get("title")
            ])

    # Print number of tasks
    print("Number of tasks in CSV: {}".format(len(user_tasks)))
