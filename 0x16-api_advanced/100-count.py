#!/usr/bin/python3
'''
A module containing functions for working with the Reddit API.
'''
import requests


def sort_histogram(histogram={}):
    '''
    Arranges and outputs the provided histogram in a sorted manner.
    '''
    # Filter out entries with a count of 0.
    histogram = list(filter(lambda kv: kv[1], histogram))
    histogram_dict = {}
    for item in histogram:
        # Sum up counts for duplicate items.
        if item[0] in histogram_dict:
            histogram_dict[item[0]] += item[1]
        else:
            histogram_dict[item[0]] = item[1]
    # Sort the histogram first by key (word) in ascending order,
    # then by value (count) in descending order.
    histogram = list(histogram_dict.items())
    histogram.sort(
        key=lambda kv: kv[0],
        reverse=False
    )
    histogram.sort(
        key=lambda kv: kv[1],
        reverse=True
    )
    # Create a string representation of the sorted histogram and print it.
    res_str = '\n'.join(list(map(
        lambda kv: '{}: {}'.format(kv[0], kv[1]),
        histogram
    )))
    if res_str:
        print(res_str)


def count_words(subreddit, word_list, histogram=[], n=0, after=None):
    '''
    Calculates the occurrences of each word from a provided word
    list within a specified subreddit's content.
    '''
    # Define headers for Reddit API request.
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
    # Define sorting and limit parameters for Reddit API request.
    sort = 'hot'
    limit = 30
    # Make a GET request to the Reddit API.
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
            'https://www.reddit.com',
            subreddit,
            sort,
            limit,
            n,
            after if after else ''
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if not histogram:
        # Convert word_list to lowercase for case-insensitive matching.
        word_list = list(map(lambda word: word.lower(), word_list))
        # Initialize the histogram with word counts set to 0.
        histogram = list(map(lambda word: (word, 0), word_list))
    if res.status_code == 200:
        # Extract data and posts from the JSON response.
        data = res.json()['data']
        posts = data['children']
        titles = list(map(lambda post: post['data']['title'], posts))
        # Update word counts in the histogram based on post titles.
        histogram = list(map(
            lambda kv: (kv[0], kv[1] + sum(list(map(
                lambda txt: txt.lower().split().count(kv[0]),
                titles
            )))),
            histogram
        ))
        if len(posts) >= limit and data['after']:
            # If there are more posts to fetch, recursively call count_words.
            count_words(
                subreddit,
                word_list,
                histogram,
                n + len(posts),
                data['after']
            )
        else:
            # Sort and print the final histogram.
            sort_histogram(histogram)
    else:
        # Handle API request failure.
        return
