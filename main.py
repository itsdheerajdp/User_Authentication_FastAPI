from fastapi import FastAPI,Depends
import models
from database import engine
from routers import authentication,user,blog
models.Base.metadata.create_all(bind=engine)
app=FastAPI()
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(blog.router)




    