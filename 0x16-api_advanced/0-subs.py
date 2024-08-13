#!/usr/bin/python3
"""
Module to query Reddit API for the number of subscribers.
"""


import requests


def number_of_subscribers(subreddit):
    """
    This queries the Reddit API and returns the subscribers of a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'Custom User-Agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
