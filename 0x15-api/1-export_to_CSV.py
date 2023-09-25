#!/usr/bin/python3
'''
A script that gathers data from an API and exports it in CSV format.
'''

import csv
import re
import requests
import sys

# The URL of the API we are querying
API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            # Fetch user data from the API
            user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
            # Fetch all todos from the API
            todos_res = requests.get('{}/todos'.format(API_URL)).json()
            # Extract the user's name from the user data
            user_name = user_res.get('name')
            # Filter todos by the user's ID
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            # Filter completed todos
            todos_done = list(filter(lambda x: x.get('completed'), todos))

            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(todos_done),
                    len(todos)
                )
            )
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))

            # Export data to CSV file
            csv_file_name = f'{id}.csv'
            with open(csv_file_name, mode='w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                # Write the header row
                csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
                # Write data for completed tasks
                for todo_done in todos_done:
                    csv_writer.writerow([id, user_name, "Completed", todo_done.get('title')])

            print(f'Data exported to {csv_file_name}')
        else:
            print('Invalid user ID provided.')
    else:
        print('Please provide a user ID as a command-line argument.')
