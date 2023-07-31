from xml.etree.ElementTree import fromstring
from typing import List
import pandas as pd
from bs4 import BeautifulSoup
import requests
from textblob import TextBlob
from bias import BiasDetector
from summarize import Summarizer
from datetime import datetime, timezone

from scraping.scrape import Scraper

class ArticleParser:
    """
    example:
    <title>Uxbridge by-election: Ulez expansion blamed for Labour loss - BBC</title>
<link>https://news.google.com/rss/articles/CBMiL2h0dHBzOi8vd3d3LmJiYy5jby51ay9uZXdzL3VrLXBvbGl0aWNzLTY2MjY0ODkz0gEzaHR0cHM6Ly93d3cuYmJjLmNvLnVrL25ld3MvdWstcG9saXRpY3MtNjYyNjQ4OTMuYW1w?oc=5</link>
<guid isPermaLink="false">2249345679</guid>
<pubDate>Fri, 21 Jul 2023 08:25:43 GMT</pubDate>
<description><ol><li><a href="https://news.google.com/rss/articles/CBMiL2h0dHBzOi8vd3d3LmJiYy5jby51ay9uZXdzL3VrLXBvbGl0aWNzLTY2MjY0ODkz0gEzaHR0cHM6Ly93d3cuYmJjLmNvLnVrL25ld3MvdWstcG9saXRpY3MtNjYyNjQ4OTMuYW1w?oc=5" target="_blank">Uxbridge by-election: Ulez expansion blamed for Labour loss</a>&nbsp;&nbsp;<font color="#6f6f6f">BBC</font></li><li><a href="https://news.google.com/rss/articles/CCAiC0l2Z1BvamdCdXNjmAEB?oc=5" target="_blank">Everything you need to know about the by-elections</a>&nbsp;&nbsp;<font color="#6f6f6f">The Times and The Sunday Times</font></li><li><a href="https://news.google.com/rss/articles/CBMiNGh0dHBzOi8vd3d3LmJiYy5jby51ay9uZXdzL2xpdmUvdWstcG9saXRpY3MtNjYxODEzMTXSAQA?oc=5" target="_blank">Labour and Lib Dems celebrate big by-election wins in Tory safe seats</a>&nbsp;&nbsp;<font color="#6f6f6f">BBC</font></li><li><a href="https://news.google.com/rss/articles/CBMiVGh0dHBzOi8vd3d3LmNpdHlhbS5jb20veW91LXdpbi1zb21lLXVsZXotc29tZS1hLW1peGVkLWJhZy1idXQtd2hhdC1kb2VzLWl0LWFsbC1tZWFuL9IBAA?oc=5" target="_blank">You win some, ULEZ some: A mixed bag of by-election results but what does it all mean? - CityAM</a>&nbsp;&nbsp;<font color="#6f6f6f">City A.M.</font></li><li><a href="https://news.google.com/rss/articles/CBMiYWh0dHBzOi8vd3d3Lm5ld3N0YXRlc21hbi5jb20vcXVpY2tmaXJlLzIwMjMvMDcvdGhlLWJ5LWVsZWN0aW9uLXJlc3VsdHMtd2lsbC10ZXJyaWZ5LW1vc3QtdG9yeS1tcHPSAQA?oc=5" target="_blank">Most Tory MPs will be terrified by the by-election results</a>&nbsp;&nbsp;<font color="#6f6f6f">The New Statesman</font></li><li><strong><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lQbGNtd0NCR1V0SnhRbHNRdmRTZ0FQAQ?hl=en-GB&gl=GB&ceid=GB:en&oc=5" target="_blank">View Full coverage on Google News</a></strong></li></ol></description>
<source url="https://www.bbc.co.uk">BBC</source>
    """

    def __init__(self, item):
        self.item = item
        self.dict = {}

    def __find(self, tag):
        return self.item.find(tag).text

    @property
    def body_text(self):
        if 'body_text' not in self.dict:
            self.dict['body_text'] = self._compute_body_text()
        return self.dict['body_text']

    @property
    def title(self):
        return self.__find('title')

    @property
    def link(self):
        return self.__find('link')

    @property
    def description(self):
        description = self.__find('description')
        return description

    @property
    def pub_date(self):
        return pd.to_datetime(self.__find('pubDate'))

    @property
    def source(self):
        return self.__find('source')
    
    def _compute_body_text(self):
        response = requests.head(self.link, allow_redirects=True)
        while 'Location' in response.headers:
            new_url = response.headers['Location']
            response = requests.head(new_url, allow_redirects=True)
        final_url = response.url
        html_text = requests.get(final_url, allow_redirects=True)

        soup = BeautifulSoup(html_text.content.decode('utf-8'), features='html.parser')
        body = soup.find_all('p')
        lists = soup.find_all('li')
        return ' '.join([p.text for p in body]) + " " + ' '.join([p.text for p in lists])

    @property
    def sentiment(self):
        """
        Finds the sentiment (polarity, subjectivity) where the polarity
        is [-1.0, 1.0] and the subjectivity is 0.0, 1.0]. Returns a named tuple
        of the form Sentiment(polarity, subjectivity). 
        """
        text_blob_object = TextBlob(self.body_text) 
        sentiment = text_blob_object.sentiment
        return sentiment
    
    @property
    def bias(self):
        """Returns the political bias of the article's source"""
        bias_detector = BiasDetector()
        bias = bias_detector.find_bias(self.source)
        return bias

    @property
    def summary(self):
        # need to physically paste in the key for demo into summarize.py
        summarizer = Summarizer()
        return summarizer.summarize(self.body_text)

    def to_search_dict(self) -> dict:
        """ Converts this 'Article' into a dict with every field that needs to be displayed in the search page"""
        dict = {
            'title': self.title,
            'link': self.link,
            'description': self.description,
            'date': self.pub_date.strftime('%Y-%m-%d %H:%M:%S'),
            'source': self.source,
            'sentiment': self.sentiment,
            'bias': self.bias
        }
        return dict

    def to_home_dict(self) -> dict:
        """Converts this 'Article' into a dict with every field that needs to be displayed in the home page"""
        today = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
        days_difference = abs((self.pub_date - today).days)
        return { 
            'title': self.title,
            'source': self.source,
            'date': f'{days_difference} days ago',
            'link': self.link
        }

    def text_description(self) -> str:
        return Scraper().get_desc_text(self.description)

def parse_news_items(not_response) -> List[ArticleParser]:
    """
    Parses the news items from the XML root element.
    """
    if not_response.status_code != 200:
        raise Exception('Failed to fetch news items.')
    root = fromstring(not_response.text)
    news_items = []
    for item in root.findall('.//channel/item'):
        article = ArticleParser(item)
        news_items.append(article)
    return news_items

