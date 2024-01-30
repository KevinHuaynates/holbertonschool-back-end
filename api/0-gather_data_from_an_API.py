#!/usr/bin/python3
"""
Gather employee TODO list progress from the REST API
"""

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
    employee_name = user_data.get("name")

    # Get TODO list
    todo_response = requests.get("{}/todos?userId={}".format(api_url,
                                                             employee_id))
    todo_data = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task.get("completed"))

    # Display results
    print("Employee {} is done with tasks({}/{}):".format
          (employee_name, completed_tasks, total_tasks))
    for task in todo_data:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
