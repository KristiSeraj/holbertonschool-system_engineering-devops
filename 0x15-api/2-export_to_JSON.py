#!/usr/bin/python3
"""Importing requests module"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    usr = requests.get("{}/users/{}".format(url, argv[1]))
    todo_url = requests.get("{}/todos?userId={}".format(url, argv[1]))
    employee_username = usr.json()
    todos_of_employee = todo_url.json()
    new_data = []
    for task in todos_of_employee:
        new_data.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_username['username']
            })
    data_json = {argv[1]: new_data}
    with open(str(argv[1]) + '.json', 'w') as f:
        json.dump(data_json, f)
