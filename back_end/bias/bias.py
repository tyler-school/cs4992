#Libraries
import pandas as pd
from textblob import TextBlob
from nltk.corpus import stopwords

# Importing the bias dataset 
__bias_dataset = pd.read_csv("back_end/bias/allsides.csv")
__bias_dataset = __bias_dataset.reset_index()

# Stops words set into upper case
stop = set(word.upper() for word in stopwords.words("english"))

def __process_source(source):
    """
    Processes the given source into uppercase tokens and returns the set with
    stop words removed using set difference operation.
    """
    text_blob = TextBlob(source.upper())
    tokens = set(text_blob.words)
    return tokens - stop

# Preprocess bias_dataset names and stores it in a set
__processed_sources = {
    tuple(__process_source(row["name"])): row["bias"]
    for _, row in __bias_dataset.iterrows()
}

def __is_subset(source, candidate_source):
    """
    Determines if all the elements in the candidate source are present in the source.
    """
    return all(token in source for token in candidate_source)

def find_bias(source):
    """
    Finds the bias level based on the source given as a string. If the source is not 
    in the table, returns unknown, otherwise returns the bias as a string.
    """
    given_source = __process_source(source)

    # Check if the preprocessed source is a subset of the processed source
    for candidate_source in __processed_sources:
        if __is_subset(given_source, candidate_source):
            return __processed_sources[candidate_source]

    return "UNKNOWN"