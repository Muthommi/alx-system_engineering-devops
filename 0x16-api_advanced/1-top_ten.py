#!/usr/bin/python3
"""
Module to query Reddit API and print 10 hot posts
"""


import requests


def top_ten(subreddit):
    """
    This queris the reddit API and prints 10 hot posts
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User-Agent'}
    params = {'limit': 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print("None")
    except requests.RequestException:
        print("None")
