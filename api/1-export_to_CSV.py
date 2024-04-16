#!/usr/bin/python3
"""Using what you did in the task #0, extend your
Python script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME",
"TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv"""
import csv
import requests
from sys import argv


api = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    """Retrieving tasks for a specific user"""
    user = requests.get(f'{api}/users/{argv[1]}').json()
    todo_list = requests.get(f"{api}/todos?userId={argv[1]}").json()

    """Writing data to a CSV file"""
    with open(f'{argv[1]}.csv', mode='w') as csvfile:
        """QUOTE = all values will be enclosed in double quotes to avoid
        problems with special characters or delimiters"""
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo_list:
            csvwriter.writerow([
                user['id'],
                user['username'],
                task['completed'],
                task['title']
            ])
