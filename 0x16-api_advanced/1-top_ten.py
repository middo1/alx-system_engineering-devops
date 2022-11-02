#!/usr/bin/python3
"""Function that returns the top 10 hottest topicsi a subreddit"""
import requests


def top_ten(subreddit):
    "returns the top 10 hottest topics in a subreddit"
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.ap1.advanced.v1.0.0 (by middo)"
    }
    params  = {
        "limit":10
    }
    res = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if res.status_code == 404:
        print('None')
        return
    results = res.json().get("data")
    [print(child.get("data").get("title")) for child in results.get("children")]
