#!/usr/bin/python3
'''
write a function that queries the Reddit API and
returns the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
'''


def number_of_subscribers(subreddit):
    '''queries the Reddit API and returns the number of subscribers'''
    from requests import get

    sub_info = get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                   headers={'User-Agent': 'My-User-Agent'},
                   allow_redirects=False)

    if sub_info.status_code > 200:
        return 0

    return sub_info.json()['data']['subscribers']
