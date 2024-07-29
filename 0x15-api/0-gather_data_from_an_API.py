#!/usr/bin/python3
"""
This module fetches and displays TODO list progress for a given employee ID
using the JSONPlaceholder API.
"""

import json
import sys
import urllib.request


def fetch_employee_todo_progress(employee_id):
    """
    Fetches and prints the TODO list progress of an employee.
    """
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = (
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    )

    try:
        with urllib.request.urlopen(user_url) as response:
            user_data = json.load(response)
        with urllib.request.urlopen(todos_url) as response:
            todos_data = json.load(response)
    except urllib.error.HTTPError:
        print("User not found")
        return

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
