# Dependency imports
from fastapi import FastAPI              # Core FastAPI class used to create the app instance
from . import models                     # Imports SQLAlchemy models (tables definitions)
from .database import engine             # Database engine used to connect to the DB
from  .routers import blog ,user         # Imports router modules for blog and user endpoints

# App instance
app = FastAPI(debug=True)                # Creates the FastAPI application (debug enabled)

# Register API routers
app.include_router(blog.router)          # Attaches blog-related routes to the main app
app.include_router(user.router)          # Attaches user-related routes to the main app

# Create database tables
models.Base.metadata.create_all(engine)  # Creates all tables defined in models (runs at startup)




