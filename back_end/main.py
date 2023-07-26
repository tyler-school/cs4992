from fastapi import FastAPI
from datetime import datetime, timedelta
from search import SearchEngine
from article import ArticleParser
from typing import List
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, ValidationError
from json import load
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
    return {"message": "Root API call"}

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
    """
    Reads from the home page JSON. If the user exists, returns the home
    page data as a list of searches, else errors.
    """
    try:
        with open('home_page.json') as file:
            data = load(file)
            user_data = HomePage(**data["home_page"]) 

            if user_data.username == username: 
                return user_data.searches
            else:
                raise HTTPException(status_code=404, detail=f"User '{username}' not found")
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="File not found")
    except ValidationError as ve:
        raise HTTPException(status_code=500, detail="Error reading data: Invalid JSON format")
    

    
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

