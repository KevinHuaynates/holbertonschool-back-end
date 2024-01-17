#!/usr/bin/python3
"""
Script to gather data from a REST API and export TODO list progress to CSV for a given employee ID.
"""

import requests
import sys
import csv

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

def export_to_csv(employee_id, todo_data):
    """
    Export TODO list progress to CSV for a given employee.

    Args:
        employee_id (int): The ID of the employee.
        todo_data (list): A list containing data about the employee's TODO list.
    """
    employee_name = todo_data[0]['username']
    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Write header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write data
        for task in todo_data:
            csv_writer.writerow([employee_id, employee_name, str(task['completed']), task['title']])

    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_todo_data = get_employee_data(employee_id)
    export_to_csv(employee_id, employee_todo_data)

