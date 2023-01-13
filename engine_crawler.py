import snscrape.modules.twitter as crawler
import re
import pandas as pd


def remove_backslash_n(value):
    return ' '.join(value.splitlines())


query = '("kinerja polri" OR "kinerja polisi")'
time_start = '2022-10-01'
time_end = '2022-12-31'
file_name = r'crawling twitter kinerja polisi or kinerja polri.xlsx'
tweet_list = []
sheet_name = "data oktober 2022"


for i, tweet in enumerate(
        crawler.TwitterSearchScraper(f'{query} until:{time_end} since:{time_start}').get_items()):
    if i > 10000:
        break
    result = tweet.content.lower()
    result = re.sub(r'(@|https?)\S+|#', '', result)
    result = result.replace("&amp;", "dan")
    result = remove_backslash_n(result)
    result = result.strip()
    tweet_list.append(result)


print(f"{len(tweet_list)} tweets scraped!")
print("removing duplicate tweets")
result_ = list(set(tweet_list))
print(f"{len(tweet_list)} tweets left after cleaning")
data_frame = pd.DataFrame(result_)
data_frame.to_excel(file_name, sheet_name=sheet_name, index=False)
