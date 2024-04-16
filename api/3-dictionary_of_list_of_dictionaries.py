#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export
data in the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json"""
import json
import requests
from sys import argv


api = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    """Retrieving all users"""
    reponse_users = requests.get(f'{api}/users')
    users = reponse_users.json()

    all_user_tasks = {}

    """Iterate over each user"""
    for user in users:
        user_id = user['id']
        username = user['username']

        """Retrieve tasks for this user"""
        response_todo = requests.get(f'{api}/todos?userId={user_id}')
        tasks = response_todo.json()

        """Prepare tasks list for this user"""
        user_tasks = []
        for task in tasks:
            user_tasks.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })

        """Store user tasks in the dictionary with user_id as key"""
        all_user_tasks[user_id] = user_tasks

    """Write all_user_tasks to a JSON file"""
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_user_tasks, jsonfile)
