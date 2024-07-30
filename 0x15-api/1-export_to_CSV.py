#!/usr/bin/python3
"""
This module fetched and displays TODO list progress and also exports data
To a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()

    if not user_data:
        print("Employee ID not found.")
        sys.exit(1)

    employee_name = user_data.get('username')

    todos_url = "{}/todos".format(base_url)
    todos_response = requests.get(todos_url, params={'userId': employee_id})
    todos_data = todos_response.json()

    csv_filename = "{}.csv".format(employee_id)

    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                employee_name,
                task.get('completed'),
                task.get('title')
            ])

    print("Data exported to {}.".format(csv_filename))
