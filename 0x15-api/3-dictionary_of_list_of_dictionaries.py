#!/usr/bin/python3
"""Importing requests module"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    usr = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    employee_data = requests.get(usr).json()
    todos_of_employee = requests.get(todo_url).json()
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
