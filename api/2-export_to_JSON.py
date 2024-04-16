#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ... ]}
File name must be: USER_ID.json"""
import json
import requests
from sys import argv


api = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    """Retrieving data for a specific user"""
    reponse_user = requests.get(f'{api}/users/{argv[1]}')
    user = reponse_user.json()

    """Retrieval tasks for a specific user"""
    reponse_todos = requests.get(f'{api}/todos?userId={argv[1]}')
    tasks = reponse_todos.json()

    """JSON data preparation"""
    user_tasks = []
    for task in tasks:
        user_tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user['username']
        })

    user_data = {argv[1]: user_tasks}

    """Writing data to a JSON file"""
    with open(f'{argv[1]}.json', 'w') as filejson:
        json.dump(user_data, filejson)
