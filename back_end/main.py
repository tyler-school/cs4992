from fastapi import FastAPI
from datetime import datetime
from search import SearchEngine
from article import ArticleParser
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"Root API call"}

@app.get("/other")
def read_other():
    return {"Other API call"}

@app.get("/search/{term}/{start_date}/{end_date}")
def read_search(term, start_date, end_date, max_results=15):

    searcher = SearchEngine(max_results=int(max_results))
    
    start_date_object = datetime.strptime(start_date, '%Y-%m-%d') # 2021-01-28
    end_date_object = datetime.strptime(end_date, '%Y-%m-%d')
    result: List[ArticleParser] = searcher.get_news(term, start_date_object, end_date_object)

    return [a.text_description() for a in result]

    


    

    