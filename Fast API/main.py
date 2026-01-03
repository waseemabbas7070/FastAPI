
from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def index():
    return {'data':{'name':'Waseen Abbas','age':24}}

@app.get("/about")
def about():
    return "This is a sample FastAPI application."
    