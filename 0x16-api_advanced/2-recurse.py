#!/usr/bin/python3
"""API Reddit"""
import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the title of all host articles"""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url=url, headers=headers)
    if response.status_code == 404:
        return None
    subs = response.json().get("data")
    for post in subs.get("children"):
        post_details = post.get("data")
        hot_list.append(post_details.get("title"))
    return hot_list
