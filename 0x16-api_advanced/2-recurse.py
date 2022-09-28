#!/usr/bin/python3
"""API Reddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list containing the title of all host articles"""

    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url=url, headers=headers)
    if response.status_code == 404:
        return None
    if after is None:
        return hot_list
    for post in response.json().get("data").get("children"):
        hot_list.append(post.get("data").get("title"))
    after = response.json().get("data").get("after")
    recurse(subreddit, hot_list, after)
    return hot_list
