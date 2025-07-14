#!/usr/bin/python3
"""
Fetch and print top 10 hot posts from a subreddit using Reddit API.
"""

import requests


def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {
        'User-Agent': 'python:subreddit.top_ten:v1.0 (by /u/your_reddit_username)'
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()

    posts = data.get('data', {}).get('children', [])

    if not posts:
        print(None)
        return

    for post in posts:
        print(post['data']['title'])
