from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Root API call"}

@app.get("/other")
def read_other():
    return {"Other API call"}