#!/usr/bin/python3
"""
Module to query Reddit API and print sorted count of keywords
"""


import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API and prints a sorted count of
    given keywords
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

            # Initialize word count dictionary
            if not word_count:
                word_count = {word.lower(): 0 for word in word_list}

            # Count keywords in titles
            for post in posts:
                title = post.get('data', {}).get('title', '').lower().split()
                for word in title:
                    if word in word_count:
                        word_count[word] += 1

            after = data.get('data', {}).get('after')
            if after is not None:
                return count_words(subreddit, word_list, after, word_count)
            else:
                sorted_counts = sorted(
                    word_count.items(), key=lambda x: (-x[1], x[0])
                )
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            return None
    except requests.RequestException:
        return None
