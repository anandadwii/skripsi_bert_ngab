import snscrape.modules.twitter as crawler
import re


def remove_n(value):
    return ' '.join(value.splitlines())


query = 'kinerja polri'
time_start = '2022-01-06'
time_end = '2022-01-07'
tweet_list = []

for i, tweet in enumerate(
        crawler.TwitterSearchScraper(f'{query} until:{time_end} since:{time_start}').get_items()):
    if i > 100:
        break
    result = tweet.content.lower()
    result = re.sub(r'(@|https?)\S+|#','',result)
    # result = re.sub(r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)', '', result)
    # reuslt = re.sub(r'@\w+', '', result)
    result = remove_n(result)
    result = result.strip()
    tweet_list.append(result)
    set(tweet_list)

print(tweet_list)
