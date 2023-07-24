import requests
import json
import pandas as pd
import time
import xml.etree.ElementTree as ET
from enums import RecentPeriod
from article import ArticleParser, parse_news_items

from datetime import datetime, timedelta

class SearchEngine:

    def __init__(self, max_results: int = 1000):
        self.max_results = max_results


    def _generate_search_url(
        self,
        search_term: str,
        start_date: datetime = None,
        end_date: datetime = None,
        period: RecentPeriod = None):
        """
        Generates a search URL for the given search term and data filter.
        If neither start_date nor end_date are passed, no time filter will be applied.
        Args:
            search_term: The term to search for.
            start_date: The start date for the search.
            end_date: The end date for the search. Defaults to today if start date is passed.
            period: A RecentPeriod enum value indicating a period length from before today to
            filter by.
        """
        if period is not None:
            if start_date is not None or end_date is not None:
                raise Exception("Cannot specify both a period and a start/end date.")
            start_date, end_date = period.get_date_range()

        elif start_date is not None:
            end_date = datetime.today() if end_date is None else end_date

        if start_date is not None and end_date is not None:
            start_string = start_date.strftime('%Y-%m-%d')
            end_string = end_date.strftime('%Y-%m-%d')
            time_filter = f'after:{start_string} before:{end_string}'
        else:
            time_filter = ''
        url = (f'https://news.google.com/rss/search?q={search_term}+{time_filter}'
               f'&hl=en-US&gl=US&ceid=US:en')
        return url

    def get_news(self,
                 search_term: str,
                 start_date_object: datetime = None,
                 end_date_object: datetime = None,
                 period: RecentPeriod = None):
        """
        Searches Google News for the given search term and data filter, and returns
        a DataFrame containing the news items.
        """
        url = self._generate_search_url(search_term=search_term,
                                        start_date=start_date_object,
                                        end_date=end_date_object,
                                        period=period)
        
        print(f"url: {url}")
        response = requests.get(url)
        news_items = parse_news_items(response) # might be an issue to hold every article as a class object within a list (RAM usage)
        # right now we can't even get that many articles, so it's not a problem
        # streaming by making a generator (iterator) might be future solution look up (def __enter__ too)
        print(a.to_dict() for a in news_items)
        return news_items

if __name__ == '__main__':
    start_time = time.time()
    news = SearchEngine()
    # search_term = input('Enter your search term here: ')
    # data_filter = int(input('Enter number of days ago or leave blank for all data: ')) or None
    search_term = 'mercedes vortices'
    news.get_news(search_term, period=RecentPeriod.THIS_MONTH)
    end_time = time.time()
    print(f'Execution time: {end_time - start_time:.2f} seconds')
