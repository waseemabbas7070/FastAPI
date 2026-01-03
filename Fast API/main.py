# Import FastAPI framework class. FastAPI handles routing, request parsing, and response generation.

from fastapi import FastAPI 

# Create an instance of FastAPI.

app = FastAPI() 

# This instance 'app' is your main application object.
# It stores all routes, middleware, exception handlers, and startup/shutdown events.

@app.get("/") 

# Define a GET endpoint for the root URL "/".
# FastAPI uses this decorator to register the function below as the handler for GET requests at "/".

def index():
    # This function runs when someone visits "http://<host>:<port>/" with GET request.
    return {'data':{'name':'Waseen Abbas','age':24}}  
    # Returns a Python dictionary.
    # FastAPI automatically converts it to JSON response.
    # The response will have content-type application/json.

@app.get("/about") 
# Define a GET endpoint for "/about" URL.
def about():
    # This function runs when someone visits "http://<host>:<port>/about".
    return "This is a sample FastAPI application."  
    # Returns a plain string.
    # FastAPI converts it to a JSON response by default.
    # Status code defaults to 200 OK.
