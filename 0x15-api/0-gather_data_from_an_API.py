#!/usr/bin/python3
'''A script that gathers data from an API.
'''
import requests
import json

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data["name"]

    # Fetch user's TODO list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Calculate TODO list progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])

    # Print progress information
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    print(f"{employee_name} ({completed_tasks}/{total_tasks}):")

    # Print completed task titles
    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_employee_todo_progress(employee_id)
