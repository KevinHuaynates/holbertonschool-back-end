#!/usr/bin/python3
import requests
import sys


def get_employee_data(employee_id):
    # URL de la API proporcionada
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Realizar la solicitud GET a la API
    response = requests.get(api_url)

    # Verificar si la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data for employee ID {employee_id}")
        sys.exit(1)


def display_todo_progress(employee_id, todo_data):
    # Filtrar tareas completadas
    completed_tasks = [task for task in todo_data if task['completed']]

    # Obtener información para el formato de salida
    employee_name = todo_data[0]['username']
    total_tasks = len(todo_data)
    completed_task_count = len(completed_tasks)

    # Imprimir el progreso de la lista de tareas
    print(f"Employee {employee_name} is done with tasks({completed_task_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    # Verificar si se proporciona el ID del empleado como argumento
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Obtener el ID del empleado desde el argumento de línea de comandos
    employee_id = int(sys.argv[1])

    # Obtener datos de la API
    employee_todo_data = get_employee_data(employee_id)

    # Mostrar el progreso de la lista de tareas
    display_todo_progress(employee_id, employee_todo_data)
