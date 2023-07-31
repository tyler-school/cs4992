#Libraries
from textblob import TextBlob

class Sentiment:
    @staticmethod
    def get_sentiment(text):
        """
        Finds the sentiment (polarity, subjectivity) where the polarity
        is [-1.0, 1.0] and the subjectivity is 0.0, 1.0]. Returns a tuple in the form (polarity, subjectivity). 
        -1 in polarity indicates negative sentiment, and 1 in polarity indicates positive sentiment
        """
        text_blob_object = TextBlob(text) 

        return text_blob_object.sentiment 