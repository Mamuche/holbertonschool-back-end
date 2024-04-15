#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress.

Requirements:

You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee
TODO list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with
tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum
of completed and non-completed tasks
Second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)"""
import requests
from sys import argv


api = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    """Retrieving tasks for a specific user"""
    todos = requests.get(f'{api}/todos?userId={argv[1]}')
    todos_data = todos.json()

    """Retrieval of user information"""
    users = requests.get(f'{api}/users/{argv[1]}')
    users_data = users.json()

    """Filtering completed tasks"""
    completed_tasks = [task for task in todos_data if task['completed']]

    user_name = users_data["name"]
    len_completed_tasks = len(completed_tasks)
    total_todo = len(todos_data)

    print("Employee {} is done with tasks({}/{}):".format(
            user_name,
            len_completed_tasks,
            total_todo))

    for task in completed_tasks:
        print(f"\t {task['title']}")
