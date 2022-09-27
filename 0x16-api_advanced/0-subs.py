#!/usr/bin/python3
"""API Reddit"""
import requests


def number_of_subscribers(subreddit):
    """Get number of subsribers for a given subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url=url, headers=headers)
    if response.status_code != 404:
        subs = response.json().get("data").get("subscribers")
        return subs
    return 0
