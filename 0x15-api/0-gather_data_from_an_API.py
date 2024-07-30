#!/usr/bin/python3
"""
This module fetches and displays TODO list progress for a given employee ID
using the JSONPlaceholder API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Prints:
        The employee's TODO list progress in the specified format.
    """
    # Fetch employee data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return
    user_data = user_response.json()
    employee_name = user_data.get('name', 'Unknown Employee')

    # Fetch TODO list for the employee
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate the number of completed tasks and total tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Print the employee TODO list progress
    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    """
    Main entry point for the script.

    Validates command-line arguments and calls the get_employee_todo_progress
    function.
    """
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
