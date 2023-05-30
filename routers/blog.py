from fastapi import APIRouter,Depends
import oauth2
import schemas
router=APIRouter()
@router.get('/blog')
def blog(current_user:schemas.User=Depends(oauth2.get_current_user)):
    return "you are logged into blog page "
