from time import time
import json
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer

"""
This program is meant to perform clustering on a list of articles, currently called contentList.
Given this list of text, it will cluster them. This creates three sets of important data (might be more to be retrived if wanted)
 - Number of articles in each cluster 
 - Words that are associated with a specific cluster
 - Articles that are in a cluster (This can be replaced with an ID to potentially make processing easier)

For the time being, this information is just printed out to the terminal. 
It could instead easily be packaged into a JSON to send to front-end. 

Issues:
The clustering program was tested with a a significant portion of wikipedia. 

The words which are associated with a cluster may not be the best topic names. 
For example, genus, family, species may show up for science/biology themed articles.
Could pre-identify these names to prettier topics, as these are very common and predictable. 

Clustering requires that a number of clusters is provided, prior to calculating them.
The number of clusters is important in regards to the accuracy of clustering, so the correct number must be chosen.

Traditionally, this is done by performing clustering with a range of cluster sizes, 
and performing an analysis to determine a knee/bend in the data slope-wise. 
This can be quite slow for larger data sets, and for some data sets no distinguishable knee exists. 

Putting an arbitrary cluster size can result in too little or too few clusters. 
Probably want to take a look at this during implementation, shouldn't be too hard to fix using sampling.

Other than that, code still has some extra stuff from tutorials in terms of benchmarking performance, and the function names and layout kind of sucks
"""

class Clustering:
    def __init__(self, contentList, true_k):
        self.clusterList = []
        self.wordList = []
        self.contentList = contentList
        self.true_k = true_k

    def fit_and_evaluate(self, km, X, name=None, n_runs=1):
        name = km.__class__.__name__ if name is None else name
        for seed in range(n_runs):
            km.set_params(random_state=seed)
            km.fit(X)

    def calculate_clusters(self):
        print("working")
        vectorizer = TfidfVectorizer(
        max_df=0.5,
        min_df=5,
        stop_words="english",
        )
        #Creates a vectorizer, setting guidelines as to how text should be processed/reduced
        vectorizer = TfidfVectorizer(
            max_df=0.5,
            min_df=5,
            stop_words="english",
        )

        #Performs the actual vectorization on the list of articles, using lsa for speed improvements
        t0 = time()
        X_tfidf = vectorizer.fit_transform(self.contentList)
        lsa = make_pipeline(TruncatedSVD(n_components=100), Normalizer(copy=False))
        t0 = time()
        X_lsa = lsa.fit_transform(X_tfidf)
        explained_variance = lsa[0].explained_variance_ratio_.sum()
        print(f"LSA done in {time() - t0:.3f} s")
        print(f"Explained variance of the SVD step: {explained_variance * 100:.1f}%")



        #Given the vectorized content, we can go about running the model
        kmeans = KMeans(
            n_clusters=self.true_k,
            max_iter=100,
            n_init=1,
        )
        self.fit_and_evaluate(kmeans, X_lsa, name="KMeans\nwith LSA on tf-idf vectors")

        #Fetch the terms associated with a cluster. This can become a cluster name.
        original_space_centroids = lsa[0].inverse_transform(kmeans.cluster_centers_)
        order_centroids = original_space_centroids.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names_out()

        for i in range(self.true_k):
            print(f"Cluster {i}: ", end="")
            self.wordList.append([])
            for ind in order_centroids[i, :10]:
                print(f"{terms[ind]} ", end="")
                self.wordList[i].append(ind)
            print()

        

        #Get what cluster a specific article is in, and print it out. 
        labels=kmeans.labels_
        clusters=pd.DataFrame(list(zip(self.contentList,labels)),columns=['title','cluster'])
        print(clusters.sort_values(by=['cluster']))


        for i in range(self.true_k):
            self.clusterList.append([])
            
        for i in range(len(clusters)):
            self.clusterList[int(clusters.iloc[i]['cluster'])].append(clusters.iloc[i]['title'])

        for i in range(self.true_k):
            print(clusters[clusters['cluster'] == i])

    def get_wordList(self):
        return self.wordList
    
    def get_contentList(self):
        return self.contentList


if __name__ == '__main__':
    contentList = []
    for x in range(1, 4):
        opener = open('./clustering/wikipediaFolder/' + str(x) + '.ext', 'r')
        fcc_data = json.load(opener)
        for i in fcc_data:
            contentList.append(i["text"])

    clustering = Clustering(contentList, 4)
    clustering.calculate_clusters()


    


       