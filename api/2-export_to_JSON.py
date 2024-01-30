#!/usr/bin/python3
"""
Export employee TODO list progress to JSON format
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])
    api_url = "https://jsonplaceholder.typicode.com"

    # Get user data
    user_response = requests.get(f"{api_url}/users/{employee_id}")
    user_data = user_response.json()
    user_id = user_data.get("id")
    user_name = user_data.get("username")

    # Get TODO list
    todo_response = requests.get(f"{api_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Filter tasks owned by the user
    user_tasks = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": user_name
        }
        for task in todo_data
        if task['userId'] == employee_id
    ]

    # Export to JSON
    json_file_name = f"{user_id}.json"
    with open(json_file_name, mode='w') as jsonfile:
        json.dump({str(user_id): user_tasks}, jsonfile)

    print(f"JSON file '{json_file_name}' created.")
