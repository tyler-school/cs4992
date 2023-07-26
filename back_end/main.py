from fastapi import FastAPI
from datetime import datetime, timedelta
from typing import List
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, ValidationError
from json import load, dumps
from pydantic import BaseModel
from search import SearchEngine
from article import ArticleParser

app = FastAPI()

class Search(BaseModel):
    term: str
    days: int
class HomePage(BaseModel):
    username: str
    searches: list[Search]
        

@app.get("/")
def read_root():
    return {"message": "Root API call"}

@app.get("/search/{term}/{days}")
def read_search(term: str, days: int, max_results: int=15):
    searcher = SearchEngine(max_results=max_results)
    news: list[ArticleParser] = searcher.get_news(term, days)

    result: list[dict] = [n.to_search_dict() for n in news]

    return dumps(result)

@app.post("/home/{username}")
def make_home_page(username: str, item: HomePage):

    # Create a new file
    home_page_file = open(f"home_pages/{username}_home_page.json", 'x')

    # Write homePage info to article
    home_page_file.write(dumps(item.model_dump()))

    return item

@app.get("/home/{username}")
def get_home_page(username: str):
    """
    Reads from the home page JSON. If the user exists, returns the home
    page data as a list of searches, else errors.
    """
    try:
        with open(f"home_pages/{username}_home_page.json") as file:
            data = load(file)
            user_data = HomePage(**data["home_page"]) 

            if user_data.username == username: 
                return get_searches(user_data.searches)
            else:
                raise HTTPException(status_code=404, detail=f"User '{username}' not found")
    except FileNotFoundError: 
       raise HTTPException(status_code=500, detail="File not found")
    except ValidationError as ve:
        raise HTTPException(status_code=500, detail="Error reading data: Invalid JSON format")
        
def get_searches(searches: dir): 
    searcher = SearchEngine(max_results=2) 
    search_data = {}
    print(searches)
    for search in searches:
        news: list[ArticleParser] = searcher.get_news(search.term, search.days)
        search_data[search.term] = [n.to_search_dict() for n in news]
    return search_data    

@app.get("home/summary")
def get_summary(item):
    item = ArticleParser(item)
    return item.summary()

@app.patch("/home/{username}")
def patch_home_page(username: str, item: HomePage):

    try:
        home_page_file = open(f"home_pages/{username}_home_page.json", 'w')
        page_obj = loads(home_page_file.read())

        (item.searches).append(page_obj["searches"])
        home_page_file.write(dumps(item.model_dump()))
        raise HTTPException(status_code=200, detail="File Successfully Updated")
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="File not found")
    except ValidationError as ve:
        raise HTTPException(status_code=500, detail="Error reading data: Invalid JSON format")
