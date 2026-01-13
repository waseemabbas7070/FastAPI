from fastapi import APIRouter , Depends , HTTPException, status
from .. import schemas , database , models
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()

get_db = database.get_db

# Show all blogs

@router.get('/blog', response_model=List[schemas.ShowBlog], tags=["Blogs"])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

# Create a blog

@router.post("/blog", status_code=status.HTTP_201_CREATED, tags=["Blogs"])
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        user_id = 1
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)  
    return new_blog

# Show a blog

@router.get('/blog/{id}', response_model=schemas.ShowBlog, tags=["Blogs"])
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with the id {id} is not available'
        )
    return blog


# Update a blog

@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=["Blogs"])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with the id {id} is not available'
        )
    blog.update(request)
    db.commit()
    return 'updated'

# Delete a blog

@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Blogs"])
def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with the id {id} is not available'
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'



