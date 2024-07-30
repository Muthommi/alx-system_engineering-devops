#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)
    
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    try:
        user = requests.get(f"{url}users/{user_id}").json()
        todos = requests.get(f"{url}todos", params={"userId": user_id}).json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    
    if not user.get("name"):
        print(f"Employee ID {user_id} not found.")
        sys.exit(1)
    
    completed = [t.get("title") for t in todos if t.get("completed")]
    total_tasks = len(todos)
    completed_tasks_count = len(completed)

    print(f"Employee {user.get('name')} is done with tasks({completed_tasks_count}/{total_tasks}):")
    for task in completed:
        print(f"\t {task}")
