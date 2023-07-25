from fastapi import FastAPI
from datetime import datetime
from search import SearchEngine
from article import ArticleParser
from typing import List
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, ValidationError
from json import load


app = FastAPI()

class Search(BaseModel):
    term: str
    days: int
class HomePage(BaseModel):
    username: str
    searches: List[Search]

@app.get("/")
def read_root():
    return {"message": "Root API call"}

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
    file_contents: dict = load(home_page_file.read())

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