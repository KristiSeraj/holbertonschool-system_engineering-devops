#!/usr/bin/python3
"""Importing requests module"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    usr = requests.get("{}/users/{}".format(url, argv[1]))
    todo_url_all = requests.get("{}/todos?userId={}".format(url, argv[1]))
    employee_name = usr.json().get("username")
    with open('{}.csv'.format(argv[1]), 'w', encoding='UTF8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in todo_url_all.json():
            writer.writerow([argv[1], employee_name,
                            i.get("completed"), i.get("title")])
