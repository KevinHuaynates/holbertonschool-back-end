#!/usr/bin/python3
"""
Export all employee TODO list progress to JSON format
"""

import json
import requests

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"

    # Get all users
    users_response = requests.get(f"{api_url}/users")
    users_data = users_response.json()

    # Create a dictionary to store tasks for all users
    all_users_tasks = {}

    for user_data in users_data:
        user_id = user_data.get("id")
        user_name = user_data.get("username")

        # Get TODO list for each user
        todo_response = requests.get(f"{api_url}/todos?userId={user_id}")
        todo_data = todo_response.json()

        # Create a list to store tasks for the current user
        user_tasks = [
            {
                "username": user_name,
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in todo_data
        ]

        # Add user tasks to the dictionary
        all_users_tasks[str(user_id)] = user_tasks

    # Export to JSON
    json_file_name = "todo_all_employees.json"
    with open(json_file_name, mode='w') as jsonfile:
        json.dump(all_users_tasks, jsonfile)

    print(f"JSON file '{json_file_name}' created.")
