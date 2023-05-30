from fastapi import APIRouter,Depends,HTTPException
import models
import schemas
from sqlalchemy.orm import Session
from database import engine,SessionLocal
from passlib.context import CryptContext
router=APIRouter(tags=['User'])
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        


# for password hashing use -> https://fastapi.tiangolo.com/lo/tutorial/security/oauth2-jwt/?h=hashing     
# encrypting password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


#creating user
@router.post('/user')
def create_user(newuser:schemas.User,db:Session=Depends(get_db)):
    hashed_password=pwd_context.hash(newuser.password)
    user_to_be_added_in_database=models.User(name=newuser.name,email=newuser.email,password=hashed_password)  
    db.add(user_to_be_added_in_database)
    db.commit()
    db.refresh(user_to_be_added_in_database)
    return user_to_be_added_in_database



# show user
@router.get('/user/{id}',response_model=schemas.ShowUser)#we want to show only name and email of user so we use response model
def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=404,detail=f"the user of id {id} is not found")
    else:
        return user
    