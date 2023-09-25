#!/usr/bin/python3
'''
Gathers data from an API and exports it to a JSON file.
'''
import json
import requests

# Define the API URL
API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    # Fetch user data from the API
    users_res = requests.get(f'{API_URL}/users').json()

    # Fetch todos data from the API
    todos_res = requests.get(f'{API_URL}/todos').json()

    # Initialize a dictionary to store user data
    users_data = {}

    # Iterate through users
    for user in users_res:
        id = user.get('id')
        user_name = user.get('username')

        # Filter todos for the given user ID
        todos = list(filter(lambda x: x.get('userId') == id, todos_res))

        # Create a list of user data (tasks and completion status)
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))

        # Add user data to the dictionary
        users_data[f'{id}'] = user_data

    # Export the user data to a JSON file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)
