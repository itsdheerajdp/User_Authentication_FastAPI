from fastapi import APIRouter,HTTPException,Depends
import schemas
from sqlalchemy.orm import Session
from database import engine,SessionLocal
import models
from passlib.context import CryptContext
from JWTToken import create_access_token
from fastapi.security import OAuth2PasswordRequestForm


router=APIRouter(tags=['Authentication'])#this tag will be visible in swagger ui of fast api



def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


#function to verify password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password) 


@router.post('/login')
def login(user: OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    userr=db.query(models.User).filter(models.User.email==user.username).first()
    if not userr:
        raise HTTPException(status_code=404,detail=f"there is no such user exists")
    if not verify_password(user.password,userr.password):
        raise HTTPException(status_code=404,detail="incorrect password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
    