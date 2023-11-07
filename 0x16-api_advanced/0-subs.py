#!/usr/bin/python3
'''
function that queries the Reddit API and returns the number of subscribers
'''
import requests


def number_of_subscribers(subreddit):
    '''This return the total number of subscribers on a given subreddit.'''
    base_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    headers = {"User-Agent": user_agent}

    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    data = response.json().get("data")
    subscribers = data.get("subscribers")
    return subscribers
