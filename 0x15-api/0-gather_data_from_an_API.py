#!/usr/bin/python3
"""Importing requests module"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    usr = requests.get("{}/users/{}".format(url, argv[1]))
    todo_url_all = requests.get("{}/todos?userId={}".format(url, argv[1]))
    todo_url = requests.get("{}/todos?userId={}&completed=true"
                            .format(url, argv[1]))
    employee_name = usr.json().get("name")
    count = len([i for i in todo_url.json()])
    count_o = len([el for el in todo_url_all.json()])
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, count, count_o))
    for i in todo_url.json():
        print("\t {}".format(i.get("title")))
