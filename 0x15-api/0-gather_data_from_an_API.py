#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and print the TODO list progress for a given employee ID."""
    url = "https://jsonplaceholder.typicode.com/"
    try:
        user_url = url + "users/{}".format(employee_id)
        todos_url = url + "todos"
        user = requests.get(user_url)).json()
        todos = requests.get(todos_url, params={"userId": employee_id}).json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return

    completed = [t.get("title") for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for c in completed:
        print("\t {}".format(c))


if __name__ == "__main__":
    """Main entry point for the script."""
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
