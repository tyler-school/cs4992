from fastapi import FastAPI
from datetime import datetime
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

@app.get("/search/{term}/{start_date}/{end_date}")
def read_search(term, start_date, end_date, max_results=15):

    searcher = SearchEngine(max_results=int(max_results))
    
    start_date_object = datetime.strptime(start_date, '%Y-%m-%d') # 2021-01-28
    end_date_object = datetime.strptime(end_date, '%Y-%m-%d')
    result: list[ArticleParser] = searcher.get_news(term, start_date_object, end_date_object)

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