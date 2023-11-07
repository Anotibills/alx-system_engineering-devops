#!/usr/bin/python3
'''
function that queries the Reddit API, parses the title of all hot articles
'''
import requests


def count_words(subreddit, word_list, instances=None, after="", count=0):
    '''
    Print counts of given words found in hot posts of a
    given Reddit subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    '''
    if instances is None:
        instances = {}

    base_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    user_agent = "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    headers = {"User-Agent": user_agent}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(base_url, headers=headers, params=params,
                            allow_redirects=False)

    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    data = results.get("data")
    after = data.get("after")
    count += data.get("dist")

    for child in data.get("children"):
        title = child.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = title.count(word.lower())
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    `if after is None:
        if len(instances) == 0:
            print("")
            return

        # Sort the instances by count, then alphabetically
        sorted_instances = sorted(instances.items(),
                                  key=lambda kv: (-kv[1], kv[0]))
        for k, v in sorted_instances:
            print("{}: {}".format(k, v))
    else:
        count_words(subreddit, word_list, instances, after, count)

# Example usage:
# subreddit = "example_subreddit"
# word_list = ["word1", "word2", "word3"]
# count_words(subreddit, word_list)
