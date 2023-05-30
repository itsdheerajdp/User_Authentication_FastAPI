from fastapi import FastAPI,Depends
import models
from database import engine
from routers import authentication,user,blog
models.Base.metadata.create_all(bind=engine)
app=FastAPI()
# code for deploy on render.com
from fastapi.middleware.cors import CORSMiddleware
origins=["*"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
@app.get('/')
def index():
    return "this is user authentication"
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(blog.router)




    