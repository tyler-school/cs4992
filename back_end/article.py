from xml.etree.ElementTree import fromstring, Element
from typing import List
import pandas as pd
from bs4 import BeautifulSoup
from pydantic import BaseModel
import requests
from textblob import TextBlob
from summarize import Summarizer
from scraping.scrape import Scraper
from bias import BiasDetector
from typing import Union
import threading

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

    def __init__(self, item: Union[dict, Element]):
        if isinstance(item, dict):
            self.item = item
        elif isinstance(item, Element):
            self.item = {'title': self.__find(item, 'title'),
                         'link': self.__find(item, 'link'),
                         'description': self.__find(item, 'description'),
                         'pub_date': self.__find(item, 'pubDate'),
                         'source': self.__find(item, 'source')}
            
    def __find(self, xml, tag):
        return xml.find(tag).text

    @property
    def title(self):
        return self.item['title']

    @property
    def link(self):
        return self.item['link']

    @property
    def description(self):
        return self.item['description']

    @property
    def pub_date(self):
        return pd.to_datetime(self.item['pub_date'])

    @property
    def source(self):
        return self.item['source']
    
    @property
    def body_text(self):
        html_text = requests.get(self.link, allow_redirects=True)
        html_text = requests.get(html_text.url, allow_redirects=True)

        soup = BeautifulSoup(html_text.content.decode('utf-8'), features='html.parser')
        body = soup.find_all('p')
        lists = soup.find_all('li')
        filtered_list = []

        # filtering out list elements with less than 2 words
        for l in lists:
            if l.text.count(" ") > 2:
                filtered_list.append(l)

        return ' '.join([p.text for p in body]) + " " + ' '.join([p.text for p in filtered_list])

    @property
    def sentiment(self):
        """
        Finds the sentiment (polarity, subjectivity) where the polarity
        is [-1.0, 1.0] and the subjectivity is 0.0, 1.0]. Returns a named tuple
        of the form Sentiment(polarity, subjectivity). 
        """
        text_blob_object = TextBlob(self.body_text) 
        return text_blob_object.sentiment
    
    @property
    def bias(self):
        """Returns the political bias of the article's source"""
        bias = BiasDetector()
        return bias.find_bias(self.source)

    def summary(self):
        # need to physically paste in the key for demo into summarize.py
        summarizer = Summarizer()
        return summarizer.summarize(self.body_text)

    def to_search_dict(self) -> dict:
        """ Converts this 'Article' into a dict with every field that needs to be displayed in the search page"""
        return {
            'title': self.title,
            'link': self.link,
            'description': self.text_description(),
            'date': self.pub_date,
            'source': self.source,
            'sentiment': self.sentiment,
            'bias': self.bias
        }
    
    def to_home_dict(self) -> dict:
        """Converts this 'Article' into a dict with every field that needs to be displayed in the home page"""
        return {
            'title': self.title,
            'source': self.source,
            'date': self.pub_date,
            'link': self.link,
            'description': self.description
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
    xml_items = []

    for item in root.findall('.//channel/item'):
        xml_items.append(item)

    def parse_list_portion(list):
        for item in list:
            article = ArticleParser(item)
            news_items.append(article)

    delegationList = [[], [], [], [], []]

    for x in range(len(xml_items)):
        delegationList[x%5].append(xml_items[x])

    t1 = threading.Thread(target=parse_list_portion, args=(delegationList[0],))
    t2 = threading.Thread(target=parse_list_portion, args=(delegationList[1],))
    t3 = threading.Thread(target=parse_list_portion, args=(delegationList[2],))
    t4 = threading.Thread(target=parse_list_portion, args=(delegationList[3],))
    t5 = threading.Thread(target=parse_list_portion, args=(delegationList[4],))
 
    # starting thread 1
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    return news_items