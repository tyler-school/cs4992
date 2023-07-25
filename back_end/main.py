from fastapi import FastAPI
from datetime import datetime
from search import SearchEngine
from article import ArticleParser
from typing import List
from pydantic import BaseModel
from json import loads


app = FastAPI()

class Search:
    term: str
    start_date: str
    end_date: str
class HomePage(BaseModel):
    username: str
    searches: List[Search]

@app.get("/")
def read_root():
    return {"Root API call"}

@app.get("/search/{term}/{start_date}/{end_date}")
def read_search(term, start_date, end_date, max_results=15):

    searcher = SearchEngine(max_results=int(max_results))
    
    start_date_object = datetime.strptime(start_date, '%Y-%m-%d') # 2021-01-28
    end_date_object = datetime.strptime(end_date, '%Y-%m-%d')
    result: List[ArticleParser] = searcher.get_news(term, start_date_object, end_date_object)

    return [a.text_description() for a in result]

@app.post("/home/{username}")
def make_home_page(
    userID: int,
    item: HomePage):
    home_page_file = open("home_page.json", 'rw')
    file_contents: dict = loads(home_page_file.read())

    return item

@app.get("/home/{username}")
def get_home_page(userID: int):
    read file
    search if user exists
    if so return home page data
    if not error    