from typing import Any
import snscrape.modules.twitter as crawler
import re
import pandas as pd
import traceback
import emoji


def preprocessing_data(text: Any) -> str:
    """"clean your data from shit"""
    result = text.lower()
    result = re.sub(r'(@|https?)\S+|#', '', result).replace("&amp;", "dan")
    result = re.sub(r'[^\w\s]', '', result)
    result = re.sub(r'\d', '', result)
    result = remove_backslash_n(result).strip()
    result = begone_emoji.sub(repl='', string=result)
    return result


def remove_backslash_n(value: str) -> str:
    """"get rid \n from string"""
    return ' '.join(value.split())


def get_emoji_regexp():
    # Sort emoji by length to make sure multi-character emojis are
    # matched first
    emojis = sorted(emoji.EMOJI_DATA, key=len, reverse=True)
    pattern = u'(' + u'|'.join(re.escape(u) for u in emojis) + u')'
    return re.compile(pattern)


begone_emoji = get_emoji_regexp()

query = '("kinerja polri" OR "kinerja polisi")'
time_start = '2022-07-01'
time_end = '2022-12-31'
file_name = r'data semester 2 2022.xlsx'
tweet_list = []
sheet_name = "data crawl jul-des 2022"
try:
    for i, tweet in enumerate(
            crawler.TwitterSearchScraper(f'{query} until:{time_end} since:{time_start}').get_items()):
        try:
            if i > 15000:
                break
            clean_tweet = preprocessing_data(tweet.content)
            tweet_list.append(clean_tweet)
        except:
            pass

    print(f"{len(tweet_list)} tweets scraped!")
    print("removing duplicate tweets")
    result_ = list(set(tweet_list))
    print(f"{len(result_)} tweets left after cleaning")
    data_frame = pd.DataFrame(result_)
    data_frame.to_excel(file_name, sheet_name=sheet_name, index=False)
    print(f"saved to{file_name}")
except:
    traceback.print_exc()
