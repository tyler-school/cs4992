from fastapi import FastAPI
import datetime
from back_end.search import SearchEngine
from back_end.article import ArticleParser
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"Root API call"}

@app.get("/other")
def read_other():
    return {"Other API call"}

@app.get("/search/{term}/{start_date}/{end_date}")
def read_search(term, start_date, end_date):

    searcher = SearchEngine()
    
    start_date_object = datetime.strptime(start_date, '%Y-%m-%d') # 2021-01-28
    end_date_object = datetime.strptime(end_date, '%Y-%m-%d')
    result: List[ArticleParser] = searcher.get_news(term, start_date_object, end_date_object)

    

    return [a.to_dict() for a in result]

    


    

    