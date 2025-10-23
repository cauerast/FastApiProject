from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def auth():
    """
    Default route
    """
    return {
            "message": "You acces the auth route",
            "auth": True,
            }