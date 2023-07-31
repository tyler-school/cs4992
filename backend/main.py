from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, ValidationError
from json import load, dumps
from pydantic import BaseModel
from search import SearchEngine
from article import ArticleParser
from fastapi.middleware.cors import CORSMiddleware
from misc_tools.summarize import Summarizer
import os

app = FastAPI()

class Article(BaseModel):
    title: str
    source: str
    date: str
    link: str
    description: str

    # def __init__(self, d: dict):
    #     self.title = d['title']
    #     self.source = d['source']
    #     self.date = d['date']
    #     self.link = d['link']
    #     self.description = d['description']

class Widget(BaseModel):
    searchTerm: str
    numberOfDays: int
    articles: list[Article]

class HomePage(BaseModel):
    widgets: list[Widget]

class SearchRequest(BaseModel):
    searchTerm: str
    numberOfDays: int
class HomePageRequest(BaseModel):
    searches: list[SearchRequest]


@app.get("/")
def read_root():
    return {"message": "Root API call"}

@app.get("/search/{term}/{days}")
def read_search(term: str, days: int, max_results: int=10):
    searcher = SearchEngine(max_results=max_results)
    news: list[ArticleParser] = searcher.get_news(term, days)
    result: list[dict] = [n.to_search_dict() for n in news]
    return result

@app.post("/home/{username}")
def make_home_page(username: str, item: HomePageRequest, max_results=10):

        # Try to create a new file for the home page
    try:
        home_page_file = open(f"home_pages/{username}_home_page.json", 'x')
    except FileExistsError as e:
        raise HTTPException(status_code=400, detail=f"Home page already exists, try GET /home/{username}")

    home_request: dict = item.model_dump()
    article_results: list[Article] = [] # title, source, date, link, description
    widgets: list[Widget] = []
    for request in home_request["searches"]:
        # request = searchTerm, numberOfDays
        searcher = SearchEngine(max_results=max_results)
        results: list[ArticleParser] = searcher.get_news(request["searchTerm"], request["numberOfDays"])
        simple_results: list[dict] = (r.to_home_dict() for r in results)

        for d in simple_results:
            article_results.append(Article(
                title=d['title'],
                source=d['source'],
                date=d['date'],
                link=d['link'],
                description=d['description']))
        
        widgets.append(Widget(searchTerm=request["searchTerm"],
                              numberOfDays=request["numberOfDays"],
                              articles=article_results))
    
    # Create the HomePage object
    home_page = HomePage(widgets=widgets)
    # String representation of the HomePage object
    dump_str = dumps(home_page.model_dump())


    # Write homePage info to article
    home_page_file.write(dump_str)

    return home_page

@app.get("/home/{username}")
def get_home_page(username: str):
    """
    Reads from the home page JSON. If the user exists, returns the home
    page data as a list of searches, else errors.
    """
    try:
        with open(os.path.join('home_pages', f'{username}_home_page.json')) as file:
            data = load(file)
            user_data = HomePage(**data)

            return user_data

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"File not found, try POST /home/{username}")
    except ValidationError as ve:
        raise HTTPException(status_code=500, detail="Error reading data: Invalid JSON format")

# Takes in the home format article dict (only technically needs link)
@app.post("/summary")
def get_summary(item: dict):
    # item: ArticleParser = ArticleParser(item)
    # item.from_dict()
    
    body_text = SearchEngine().get_body_text_from_link(item.get("link"))
    if body_text:
        return Summarizer().summarize(body_text)
    else:
        raise HTTPException(status_code=400, detail=f'Make sure a link is included in the body')
    

@app.patch("/home/{username}")
def patch_home_page(username: str, item: SearchRequest, max_results=25):
    try:
        home_page_file = open(f"home_pages/{username}_home_page.json", 'r')
    except FileExistsError as e:
        return get_home_page(username)

    home_request: dict = item.model_dump()
    article_results: list[Article] = [] # title, source, date, link, description
    widgets: list[Widget] = []

    searcher = SearchEngine(max_results=max_results)
    results: list[ArticleParser] = searcher.get_news(home_request["searchTerm"], home_request["numberOfDays"])
    simple_results: list[dict] = (r.to_search_dict() for r in results)

    for d in simple_results:
        article_results.append(Article(
            title=d['title'],
            source=d['source'],
            date=d['date'],
            link=d['link'],
            description=d["description"]))
        
    widgets.append(Widget(searchTerm=home_request["searchTerm"],
                        numberOfDays=home_request["numberOfDays"],
                        articles=article_results))

    widgetList = load(home_page_file)["widgets"]
    widgetList = widgetList + widgets

    # Create the HomePage object
    home_page = HomePage(widgets=widgetList)
    # String representation of the HomePage object
    dump_str = dumps(home_page.model_dump())

    home_page_file = open(f"home_pages/{username}_home_page.json", 'w')
    # Write homePage info to article
    home_page_file.write(dump_str)

    return widgetList

# White listing port 3000 so front end can make calls
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)