#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{api_url}/users").json()
    todo_data = requests.get(f"{api_url}/todos").json()

    user_tasks = {}

    for user in users:
        user_id = str(user["id"])
        username = user["username"]

        tasks = []
        for task in todo_data:
            if task['userId'] == user["id"]:
                task_info = {
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                }
                tasks.append(task_info)

        user_tasks[user_id] = tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file, indent=2)
        print
        (f"JSON file 'todo_all_employees.json' created for user {user_id}.")
