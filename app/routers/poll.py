from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def mypoll():
    return {"mypoll": "testing my poll"}