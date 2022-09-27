#!/usr/bin/python3
"""API Reddit"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts
    listed for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url=url, headers=headers)
    if response.status_code == 404:
        print(None)
        return
    subs = response.json().get("data")
    for post in subs.get("children"):
        post_details = post.get("data")
        print(post_details.get("title"))
