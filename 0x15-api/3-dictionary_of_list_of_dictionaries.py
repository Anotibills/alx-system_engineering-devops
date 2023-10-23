#!/usr/bin/python3
"""A script that, using a REST API, fetches TODO list"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    import json
    import requests
    import sys

    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    todoAll = {}

    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[user.get('id')] = taskList
    '''This updates the dictionary'''
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
