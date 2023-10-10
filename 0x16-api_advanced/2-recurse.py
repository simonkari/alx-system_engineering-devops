#!/usr/bin/python3

'''
A module containing functions for working with the Reddit API.
'''

# Import the requests library, which is used for making HTTP requests.
import requests

# Define the base URL for Reddit's API.
BASE_URL = 'https://www.reddit.com'


def recurse(subreddit, hot_list=[], n=0, after=None):
    '''
    Obtain a list of hot posts from a given subreddit.
    '''

    # Define the headers for the HTTP request.
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }

    # Specify sorting criteria, limit, count, and 'after' parameter
    sort = 'hot'
    limit = 30

    # Send an HTTP GET request to the Reddit API
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
            BASE_URL,
            subreddit,
            sort,
            limit,
            n,
            after if after else ''
        ),
        headers=api_headers,
        allow_redirects=False
    )

    # Check if the HTTP request was successful (status code 200).
    if res.status_code == 200:
        data = res.json()['data']
        posts = data['children']
        count = len(posts)

        # Extract the titles of the hot posts and add them to the hot_list.
        hot_list.extend(list(map(lambda x: x['data']['title'], posts)))

        # Check if there are more posts to retrieve and if 'after' is provided.
        if count >= limit and data['after']:

            # Recursively call the function to retrieve the next set of posts.
            return recurse(subreddit, hot_list, n + count, data['after'])
        else:
            # Return the hot_list if no more posts are available.
            return hot_list if hot_list else None
    else:
        # Return the hot_list if the request was not successful.
        return hot_list if hot_list else None
