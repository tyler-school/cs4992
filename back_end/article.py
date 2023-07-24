from xml.etree.ElementTree import ElementTree, fromstring
from typing import List
import datetime as dt
import pandas as pd
from bs4 import BeautifulSoup
import requests

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
        self._title = item.find('title').text
        self._link = item.find('link').text
        self._description = item.find('description').text
        self._pub_date = pd.to_datetime(item.find('pubDate').text)
        self._source = item.find('source').text

    def __find(self, tag):
        return self.item.find(tag).text

    @property
    def title(self):
        return self.__find('title')

    @property
    def link(self):
        return self.__find('link')

    @property
    def description(self):
        description = self.__find('description')
        # start = description.find('<p>') + 3
        # end = description.find('</p>')
        # return description[start:end]
        return description

    @property
    def pub_date(self):
        return pd.to_datetime(self.__find('pubDate'))

    @property
    def source(self):
        return self.__find('source')
    
    @property
    def body_text(self):
        html_text = requests.get(self._link, allow_redirects=True)
        print(html_text.url)

        html_text = requests.get(html_text.url, allow_redirects=True)
        print(html_text.url)
        
        soup = BeautifulSoup(html_text.content.decode('utf-8'))
        body = soup.find_all('p')
        lists = soup.find_all('li')
        return ' '.join([p.text for p in body]) + " " + ' '.join([p.text for p in lists])

    def to_dict(self) -> dict:
        """ Converts this 'Article' into a dict with every derivable field """
        return {
            'title': self.title,
            'link': self.link,
            'description': self.description,
            'pub_date': self.pub_date,
            'source': self.source,
            'body_text': self.body_text
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
