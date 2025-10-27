from fastapi import APIRouter, Depends
from models import User
from dependencies import get_session
from main import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home(): 
    """
    Default route
    """
    return {
            "message": "You acces the auth route",
            "auth": True,
            }

@auth_router.post("/create_account")
async def createAccount(name: str, email: str, password: str, session=Depends(get_session)):
    user = session.query(User).filter(User.email==email).first()
    if user:
        return {"message": "There is already a user with this email"}
    else:
        crypt_password = bcrypt_context.hash(password)
        new_user = User(name, email, crypt_password)
        session.add(new_user)
        session.commit()
        return {"message": "User registered successfully"}
