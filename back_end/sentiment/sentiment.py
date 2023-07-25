#Libraries
from textblob import TextBlob

class Sentiment:
    @staticmethod
    def get_sentiment(text):
        """
        Finds the sentiment (polarity, subjectivity) where the polarity
        is [-1.0, 1.0] and the subjectivity is 0.0, 1.0]. Returns a named tuple
        of the form Sentiment(polarity, subjectivity). 
        """
        text_blob_object = TextBlob(text) 

        return text_blob_object.sentiment