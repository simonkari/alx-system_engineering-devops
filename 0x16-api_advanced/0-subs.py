#!/usr/bin/python3

'''
A module that encompasses functions designed for interacting with the Reddit API.
'''

# Import the requests library, which is used for making HTTP requests.
import requests

# Specify the foundational web address for Reddit's API.
BASE_URL = 'https://www.reddit.com'

def number_of_subscribers(subreddit):
    '''
    Fetches the subscriber count for a specified subreddit
    '''
    
    # Define the headers for the HTTP request. These headers mimic a web browser user-agent.
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

    # Send an HTTP GET request to the Reddit API to retrieve information about the subreddit.
    res = requests.get(
        '{}/r/{}/about/.json'.format(BASE_URL, subreddit),
        headers=api_headers,
        allow_redirects=False
    )
    
    # Check if the HTTP request was successful (status code 200).
    if res.status_code == 200:
        
        # Parse the JSON response and extract the number of subscribers from the 'data' field.
        return res.json()['data']['subscribers']
    
    # If the request was not successful, return 0 subscribers.
    return 0
