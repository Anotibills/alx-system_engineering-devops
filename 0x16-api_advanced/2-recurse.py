#!/usr/bin/python3
'''
function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
'''
import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    '''This return a list of titles of all hot posts on a given subreddit.'''
    if hot_list is None:
        hot_list = []

    base_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    user_agent = "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    headers = {"User-Agent": user_agent}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(
        base_url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code == 404:
        return None

    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")

    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
