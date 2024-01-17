#!/usr/bin/python3
"""
Script to gather data from a REST API and display TODO list progress for a given employee ID.
"""

import requests
import sys

def get_employee_data(employee_id):
    """
    Get employee data from the API for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: A list containing data about the employee's TODO list.
    """
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data for employee ID {employee_id}")
        sys.exit(1)

def display_todo_progress(employee_id, todo_data):
    """
    Display TODO list progress for a given employee.

    Args:
        employee_id (int): The ID of the employee.
        todo_data (list): A list containing data about the employee's TODO list.
    """
    completed_tasks = [task for task in todo_data if task['completed']]

    employee_name = todo_data[0]['username']
    total_tasks = len(todo_data)
    completed_task_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({completed_task_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_todo_data = get_employee_data(employee_id)
    display_todo_progress(employee_id, employee_todo_data)

