#!/usr/bin/python3
'''Gathers data from an API and exports it to a CSV file.
'''
import re
import requests
import sys

# Define the API URL
API_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''

if __name__ == '__main__':
    # Check if command-line argument is provided
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            # Parse the user ID from the command line argument
            id = int(sys.argv[1])
            # Fetch user data from the API
            user_res = requests.get(f'{API_URL}/users/{id}').json()
            # Fetch todos data from the API
            todos_res = requests.get(f'{API_URL}/todos').json()
            user_name = user_res.get('username')
            # Filter todos for the given user ID
            todos = [todo for todo in todos_res if todo.get('userId') == id]
            with open(f'{id}.csv', 'w') as file:
                for todo in todos:
                    # Write data in CSV format
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            user_name,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )
