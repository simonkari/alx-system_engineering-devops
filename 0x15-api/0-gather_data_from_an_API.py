#!/usr/bin/python3
'''A script that gathers data from an API.
'''

import re
import requests
import sys

# The URL of the API we are querying
API_URL = 'https://jsonplaceholder.typicode.com'

def main():
    # Check if a command-line argument is provided
    if len(sys.argv) > 1:
        # Check if the provided argument is a positive integer
        if re.fullmatch(r'\d+', sys.argv[1]):
            # Convert the argument to an integer (user ID)
            user_id = int(sys.argv[1])
            
            # Fetch user data from the API
            user_res = requests.get(f'{API_URL}/users/{user_id}').json()
            
            # Fetch all todos from the API
            todos_res = requests.get(f'{API_URL}/todos').json()
            
            # Extract the user's name from the user data
            user_name = user_res.get('name')
            
            # Filter todos by the user's ID
            todos = [todo for todo in todos_res if todo.get('userId') == user_id]
            
            # Filter completed todos
            todos_done = [todo for todo in todos if todo.get('completed')]
            
            # Display the results
            print(
                f'Employee {user_name} is done with tasks ({len(todos_done)}/{len(todos)}):'
            )
            
            # Print the titles of completed todos
            for todo_done in todos_done:
                print(f'\t{todo_done.get("title")}')

if __name__ == '__main__':
    main()
