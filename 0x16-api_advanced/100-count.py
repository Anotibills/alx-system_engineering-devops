#!/usr/bin/python3
'''
function that queries the Reddit API, parses the title of all hot articles
'''
import re
import requests


def add_title(dictionary, hot_posts):
    '''
    This add words from post titles to the dictionary
    '''
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    '''
    This recursively queries the Reddit API and processes posts
    '''
    user_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': user_agent
    }

    params = {
        'after': after
    }

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(base_url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    hot_posts = data['data']['children']
    add_title(dictionary, hot_posts)
    after = data['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list, dictionary=None):
    '''
    This count word occurrences in the top posts of a subreddit
    '''
    if dictionary is None:
        dictionary = {}

    for word in word_list:
        word = word.lower()
        if word not in dictionary:
            dictionary[word] = 0

    recurse(subreddit, dictionary)

    sorted_items = sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0]))
    for item in sorted_items:
        if item[1] > 0:
            print("{}: {}".format(item[0], item[1]))
