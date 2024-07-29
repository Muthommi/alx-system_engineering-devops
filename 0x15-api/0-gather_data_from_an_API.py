#!/usr/bin/python3
"""
This module fetches and displays TODO list progress for a given employee ID
using the JSONPlaceholder API.
"""

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Fetches and prints the TODO list progress of an employee.
    """

    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = (
            f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        print("User not found")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    num_done_tasks = len(done_tasks)

    print(
        f"Employee {employee_name} is done with tasks("
        f"{num_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)
