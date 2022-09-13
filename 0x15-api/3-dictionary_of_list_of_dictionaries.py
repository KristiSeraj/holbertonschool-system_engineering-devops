#!/usr/bin/python3
"""Importing requests module"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    usr = requests.get(f"{url}/users")
    todo_url = requests.get(f"{url}/todos")
    employee_data = usr.json()
    todos_of_employee = todo_url.json()
    data_json = {}
    for user in employee_data:
        new_data = []
        for todo in todos_of_employee:
            if user['id'] == todo['userId']:
                new_data.append({
                    "username": user['username'],
                    "task": todo['title'],
                    "completed": todo['completed']
                })
        data_json[user['id']] = new_data
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data_json, f)
