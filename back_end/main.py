from fastapi import FastAPI
from typing import List
from hello import hello_function

app = FastAPI()

@app.get("/")
def read_root():
    return {"Root API call"}

@app.get("/other")
def read_other():
    return {"Other API call"}

    
@app.post("/api/hello/")
def read_hello(request_data: dict):
    name = request_data.get("name", "Guest")  # Get the "name" from request_data, default to "Guest" if not present

    # Call the hello_function with the "name" parameter and get the response message
    response_message = hello_function(name)

    return {"message": response_message}


@app.get("/other")
def read_other():
    return {"message": "Other API call"}
    

    