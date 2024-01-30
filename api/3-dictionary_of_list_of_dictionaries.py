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
                tasks.append({
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                })

        if not tasks:
            # If the user has no tasks, include an empty task entry
            tasks.append({
                "username": username,
                "task": None,
                "completed": None
            })

        user_tasks[user_id] = tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file)
        print("JSON file 'todo_all_employees.json' created.")
