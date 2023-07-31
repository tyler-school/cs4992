from textblob import TextBlob
from article import ArticleParser
from datetime import datetime, timedelta
from xml.etree.ElementTree import fromstring
import requests
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 

class SentimentOverTime:
    """Performs sentiment analysis over the defined time"""

    def __init__(self, 
                 search_term: str, 
                 start: datetime,
                 end: datetime,
                 items: int = 5):
        """Initializes the parameters for the search, and establishes start and end times if not specified explicitly"""

        if start and not end:
            # no to date, default to a timeframe of 10 days
            end = start + timedelta(days=10)
        elif end and not start:
            # no from date, default to a timeframe of 10 days
            start = end - timedelta(days=10)
        elif not end and not start:
            # neither exist, default to a timeframe of the past 10 days
            end = datetime.today()
            start = end - timedelta(days=10)

        self.start = start
        self.end = end
        self.search_term = search_term 
        self.items = items

    def generate_search_urls(self) -> list[str]:
        """
        Generates a search URL for the given search term and start and end date
        Used for sentiment analysis over time
        """

        delta = self.end - self.start

        # for every day in the range, generate a search URL for the same topic

        # specifying "pointers" to the start and end date
        from_date = self.start
        to_date = self.start + timedelta(days=1)

        urls = []

        for _ in range(delta.days):
            time_filter = f'after:{from_date.strftime("%Y-%m-%d")} before:{to_date.strftime("%Y-%m-%d")}'
            urls.append(f'https://news.google.com/rss/search?q={self.search_term}+{time_filter}&hl=en-GB&gl=GB&ceid=GB:en')
            from_date = to_date
            to_date = to_date + timedelta(days=1)

        return urls
    
    def get_x_news(self, urls: list[str]) -> list[list[ArticleParser]]:
        """
        Searches Google News for the given search term, and returns the number of news items specified. 
        """
        articles = []
        for i in range(0, len(urls)):
            response = requests.get(urls[i])
            root = fromstring(response.text)
            news_items = []
            all_items = root.findall('.//channel/item')
            for j in range(self.items):
                article = ArticleParser(all_items[j])
                news_items.append(article)
            articles.append(news_items)
        return articles
    
    def analyse_polarity(self, articles: list[list[ArticleParser]]) -> list[float]:
        """Analyses and averages the sentiment over each day, and returns a set of data points that can be used for plotting"""
        sentiments = []
        for art in articles:
            # we average the sentiment over the list art of articles
            polarity = np.mean([a.sentiment[0] for a in art])
            sentiments.append(round(polarity, 2))
        return sentiments
    
    def generate_dates(self) -> list[str]:
        """Generates a list of dates in string form used for the x axis of the graph plotted"""
        delta = timedelta(days=1)
        dates = []
        start = self.start 
        while start.date() < self.end.date():
            start += delta
            dates.append(start.strftime('%m/%d/%Y'))
        return dates
    
    def graph(self):
        """Graphs the sentiment over time for this search"""

        dates = self.generate_dates()
        polarities = self.analyse_polarity(self.get_x_news(self.generate_search_urls()))

        column_names = ['date', 'polarity']
        df=pd.DataFrame(np.transpose([dates, polarities]), columns=column_names)
        df.polarity = df.polarity.astype(float)
        
        plt.figure(figsize=(8, 4))
        plt.scatter(df['date'], df['polarity'], label='Polarity', marker='x', c='red')
        plt.xlabel("Date")
        plt.ylabel("Polarity")
        plt.title(f"Polarity over time of the topic '{self.search_term}'")
        plt.xticks([dates[0], dates[-1]])
        plt.ylim(-1, 1)
        plt.savefig(f'cs4992/back_end/sentiment_analysis_{self.search_term}.png')
        plt.show()
        plt.close()

if __name__ == '__main__':
    sentiment = SentimentOverTime("robbery", datetime.today() - timedelta(days=10), datetime.today(), 1)
    sentiment.graph()