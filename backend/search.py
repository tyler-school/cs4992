from bs4 import BeautifulSoup
import requests
import time
from article import parse_news_items

from datetime import datetime, timedelta, date

class SearchEngine:

    def __init__(self, max_results: int = 15):
        self.max_results = max_results


    def _generate_search_url(
        self,
        search_term: str,
        days: int):
        """
        Generates a search URL for the given search term and data filter.
        Args:
            search_term: The term to search for.
            days: The range of dates to search in in the past
        """
        start_string = date.today()
        # truncate at 10 to remove seconds and milliseconds
        end_string = str(datetime.today() - timedelta(days=days))[:10]

        time_filter = f'after:{end_string}+before:{start_string}'
        url = (f'https://news.google.com/rss/search?q={search_term}+{time_filter}'
               f'&hl=en-GB&gl=GB&ceid=GB:en')
        return url

    def get_news(self,
                 search_term: str,
                 days: int):
        """
        Searches Google News for the given search term and data filter, and returns
        a DataFrame containing the news items.
        """
        url = self._generate_search_url(search_term=search_term,
                                        days=days)
        
        print(f"Getting news with url: {url}")
        try:
            response = requests.get(url)
        except ConnectionError as e:
            raise ConnectionError("Network error. Check internet connection.")
        news_items = parse_news_items(response) # might be an issue to hold every article as a class object within a list (RAM usage)
        # right now we can't even get that many articles, so it's not a problem
        # streaming by making a generator (iterator) might be future solution look up (def __enter__ too)
        
        # printing all info in dict (json) format for each rss result
        #print([a.to_dict() for a in news_items])

        # For getting text descriptions:
        #print([a.text_description() for a in news_items])
        news_items = news_items[:self.max_results]
        return news_items
    
    def get_body_text_from_link(self, link_url):
        response = requests.head(link_url, allow_redirects=True)
        while 'Location' in response.headers:
            new_url = response.headers['Location']
            response = requests.head(new_url, allow_redirects=True)
        final_url = response.url
        html_text = requests.get(final_url, allow_redirects=True)

        soup = BeautifulSoup(html_text.content.decode('utf-8'), features='html.parser')
        body = soup.find_all('p')
        lists = soup.find_all('li')
        return ' '.join([p.text for p in body]) + " " + ' '.join([p.text for p in lists])

if __name__ == '__main__':
    start_time = time.time()
    news = SearchEngine()
    # search_term = input('Enter your search term here: ')
    # data_filter = int(input('Enter number of days ago or leave blank for all data: ')) or None
    search_term = 'mercedes vortices'
    news = news.get_news(search_term, days=30)
    print(news[0].body_text)
    end_time = time.time()
    print(f'Execution time: {end_time - start_time:.2f} seconds')
