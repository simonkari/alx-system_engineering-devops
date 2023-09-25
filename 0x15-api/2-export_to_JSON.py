#!/usr/bin/python3
'''
Gathers data from an API and exports it to a JSON file.
'''
import json
import re
import requests
import sys

# Define the API URL
API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    # Check if a command-line argument is provided
    if len(sys.argv) > 1:
        # Check if the argument is a valid integer
        if re.fullmatch(r'\d+', sys.argv[1]):
            # Parse the user ID from the command-line argument
            id = int(sys.argv[1])

            # Fetch user data from the API
            user_res = requests.get(f'{API_URL}/users/{id}').json()

            # Fetch todos data from the API
            todos_res = requests.get(f'{API_URL}/todos').json()

            # Extract the username of the user
            user_name = user_res.get('username')

            # Filter todos for the given user ID
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))

            # Create a JSON file with user and todos data
            with open(f'{id}.json', 'w') as file:
                user_data = list(map(
                    lambda x: {
                        'task': x.get('title'),
                        'completed': x.get('completed'),
                        'username': user_name
                    },
                    todos
                ))
                users_data = {
                    f'{id}': user_data
                }
                json.dump(users_data, file)
