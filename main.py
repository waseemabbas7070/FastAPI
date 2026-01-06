
from fastapi import FastAPI 
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI() 


@app.get("/blog") 

def index(limit):
    # only get 10 pubished blogs
    return {'data':f'{limit} from the blogs database'}  
   

@app.get('/blogs/{id}') 

def show(id :int):
    # fetch blog with id = id
    return {'data':id}
   
   
   
@app.get('/blog/unpublished')
def unpublished():
    # fetch all unpublished blogs
    return {'data':'all unpublished blogs'}
   

@app.get('/blogs/{id}/comments')
def comments(id :int):
    # fetch comments of blog with id = id
    return {'data':{'1','2'}}
    
class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]

@app.post('/blogs')
def create_blog(blog:Blog):
    return {'data':f'Blog is created with title as {blog.title}'}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
    