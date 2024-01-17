#!/usr/bin/python3
"""
Script to export data in JSON format for all tasks from all employees.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    employees = requests.get(url).json()

    all_tasks = {}

    for employee in employees:
        user_id = str(employee['id'])
        username = employee['username']

        url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
        tasks = requests.get(url).json()

        task_list = []
        for task in tasks:
            task_dict = {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            task_list.append(task_dict)

        all_tasks[user_id] = task_list

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)

