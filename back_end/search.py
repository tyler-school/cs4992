import requests
import pandas as pd
import time
import xml.etree.ElementTree as ET
from back_end.enums import RecentPeriod
from article import ArticleParser, parse_news_items

from datetime import datetime, timedelta


class BaseNewsParser:

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
                 start_date: datetime = None,
                 end_date: datetime = None,
                 period: RecentPeriod = None):
        """
        Searches Google News for the given search term and data filter, and returns
        a DataFrame containing the news items.
        """
        url = self._generate_search_url(search_term=search_term,
                                        start_date=start_date,
                                        end_date=end_date,
                                        period=period)
        response = requests.get(url)
        news_items = parse_news_items(response)
        df = pd.DataFrame(news_items)
        df.to_csv(f'{search_term}_news.csv', encoding='utf-8-sig', index=False)
        return df


if __name__ == '__main__':
    start_time = time.time()
    search_term = input('Enter your search term here: ')
    data_filter = int(input('Enter number of days ago or leave blank for all data: ')) or None
    data = get_news(search_term, data_filter)
    end_time = time.time()
    print(f'Execution time: {end_time - start_time:.2f} seconds')
