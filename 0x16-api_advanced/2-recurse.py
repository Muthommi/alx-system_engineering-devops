#!/usr/bin/python3
"""
Module to query Reddit API and return a list of titles for hot articles
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries reddit API and returns a list of titles
    for hot articles.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User-Agent'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                hot_list.append(post.get('data', {}).get('title'))
            after = data.get('data', {}).get(after)
            if after is not None:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except requests.RequestException:
        return None
