import pandas as pd
from textblob import TextBlob
from nltk.corpus import stopwords 

class BiasDetector:
    def __init__(self):
        # Libraries
        self.stop = set(word.upper() for word in stopwords.words("english")) 

        # Importing the bias dataset 
        bias_dataset = pd.read_csv("bias/allsides.csv")
        bias_dataset = bias_dataset.reset_index()

        # Preprocess bias_dataset names and stores it in a set
        self.processed_sources = {
            tuple(self.__process_source(source=row["name"])): row["bias"]
            for _, row in bias_dataset.iterrows()
        }

    def __process_source(self, source):
        """
        Processes the given source into uppercase tokens and returns the set with
        stop words removed using set difference operation.
        """
        text_blob = TextBlob(source.upper())
        tokens = set(text_blob.words)
        return tokens - self.stop

    def __is_subset(self, source, candidate_source):
        """
        Determines if all the elements in the candidate source are present in the source.
        """
        return all(token in source for token in candidate_source)

    def find_bias(self, source):
        """
        Finds the bias level based on the source given as a string. If the source is not 
        in the table, returns unknown, otherwise returns the bias as a string.
        """
        given_source = self.__process_source(source)

        # Check if the preprocessed source is a subset of the processed source
        for candidate_source in self.processed_sources:
            if self.__is_subset(source=given_source, candidate_source=candidate_source):
                return self.processed_sources[candidate_source]

        return "UNKNOWN"
