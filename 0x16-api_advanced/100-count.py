#!/usr/bin/python3
""" raddit api"""

from collections import Counter
import requests


def count_words(subreddit, word_list, hot_list=None, after=None):
    """count all words"""

    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json?limit=25".format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {
        "User-Agent": "YourUserAgent"
        }
    request = requests.get(url, headers=headers)

    if request.status_code == 200:
        data = request.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title'].lower()
                hot_list.append(title)

            after = data['data']['after']

            if after is not None:
                return count_words(subreddit, word_list, hot_list, after)
            else:
                # Combine the hot_list into a single string for word counting
                all_titles = ' '.join(hot_list)
                word_counter = Counter(all_titles.split())
                word_counts = {}

                for word in word_list:
                    count = word_counter.get(word, 0)
                    word_counts[word] = count

                sorted_word_counts = sorted(
                        word_counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_counts:
                    if count > 0:
                        print(f"{word}: {count}")

        else:
            return
    else:
        return
