#Libraries
import requests
import pandas as pd
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from datetime import datetime, timedelta

def get_sentiment(text):
    """
    Finds the sentiment (polairty, subjectivity) where the polarity
    is [-1.0, 1.0] and the subjectivity is 0.0, 1.0]. Returns a named tuple
    of the form Sentiment(polarity, subjectivity).
    """
    text_blob_object = TextBlob(text)

    return text_blob_object.sentiment