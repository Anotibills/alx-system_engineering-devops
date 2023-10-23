#!/usr/bin/python3
"""A script that, using a REST API, fetches TODO list progress"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    sessionReq = requests.Session()
    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)
    '''Gets Employees info from urlsource'''
    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = []
    updateUser = {}

    for all_Emp in json_req:
        totalTasks.append({
            "task": all_Emp.get('title'),
            "completed": all_Emp.get('completed'),
            "username": usr,
        })
    '''This provide employees info and update them'''
    updateUser[idEmp] = totalTasks

    file_Json = idEmp + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
