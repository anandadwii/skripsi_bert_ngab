import snscrape.modules.twitter as crawler
query = 'kinerja polri'
time_start = '2022-01-06'
time_end = '2022-01-07'
tweet_list = []

for i, tweet in enumerate(
        crawler.TwitterSearchScraper(f'{query} until:{time_end} since:{time_start}').get_items()):
    print(tweet)

