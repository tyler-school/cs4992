from fastapi import FastAPI
from datetime import datetime, timedelta
from search import SearchEngine
from article import ArticleParser
from pydantic import BaseModel
from json import loads, dumps


app = FastAPI()

class Search(BaseModel):
    term: str
    days: int
class HomePage(BaseModel):
    username: str
    searches: list[Search]
        

@app.get("/")
def read_root():
    return {"Root API call"}

@app.get("/search/{term}/{days}")
def read_search(term: str, days: int, max_results: int=15):

    searcher = SearchEngine(max_results=max_results)
    result: list[ArticleParser] = searcher.get_news(term, days)

    return [a.text_description() for a in result]

@app.post("/home/{username}")
def make_home_page(username: str, item: HomePage):

    # Create a new file
    home_page_file = open(f"home_pages/{username}_home_page.json", 'x')

    # Write homePage info to article
    home_page_file.write(dumps(item.model_dump()))

    return item

@app.get("/home/{username}")
def get_home_page(username: str):

    home_page_file = open(f"home_pages/{username}_home_page.json", 'r')
    page_obj = loads(home_page_file.read())

    return page_obj