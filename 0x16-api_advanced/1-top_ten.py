#!/usr/bin/python3

'''
A module with functions for working with the Reddit API.
'''

# Import the requests library, which is used for making HTTP requests.
import requests

# Define the base URL for Reddit's API.
BASE_URL = 'https://www.reddit.com'


def top_ten(subreddit):
    '''
    Obtains the titles of the highest-ranking ten posts of a given subreddit.
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

    # Specify the sorting criteria and limit for the posts.
    sort = 'top'
    limit = 10

    # Send an HTTP GET request to the Reddit API
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}'.format(
            BASE_URL,
            subreddit,
            sort,
            limit
        ),
        headers=api_headers,
        allow_redirects=False
    )

    # Check if the HTTP request was successful (status code 200).
    if res.status_code == 200:

        # Parse the JSON response and extract the titles of the top ten posts.
        for post in res.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        # If the request was not successful, print None.
        print(None)
