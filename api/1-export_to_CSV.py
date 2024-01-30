#!/usr/bin/python3
"""
Module para exportar datos de tareas de un usuario en formato CSV
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    # Obtener el ID del usuario del argumento de línea de comandos
    user_id = argv[1]

    # Construir las URLs para obtener información del usuario y tareas
    user_info_url =
    'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    tasks_url =
    'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)

    # Obtener datos del usuario y tareas
    response_user = requests.get(user_info_url)
    response_tasks = requests.get(tasks_url)

    user_data = response_user.json()
    tasks_data = response_tasks.json()

    # Obtener el nombre de usuario del objeto de datos del usuario
    username = user_data.get('username')

    # Construir el nombre del archivo CSV
    filename = '{}.csv'.format(user_id)

    # Abrir el archivo CSV para escribir
    with open(filename, mode='w', newline='') as csvfile:
        # Definir los nombres de campo para el encabezado CSV
        fieldnames = ["USER_ID",
                      "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        # Crear un escritor CSV
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Escribir el encabezado
        writer.writeheader()

        # Iterar sobre las tareas y escribir cada tarea en una fila CSV
        for task in tasks_data:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS":
                "True" if task["completed"] else "False",
                "TASK_TITLE": task["title"]
            })

    print("Number of tasks in CSV: OK")
