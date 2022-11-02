#!/usr/bin/python3
"""Function that returns the number of subcribers in a subreddit"""
import requests


def number_of_subscribers(subreddit):
    "returns the number of members in a subreddit"
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.ap1.advanced.v1.0.0 (by middo)"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    results = res.json().get("data")
    return results.get('subscribers')
