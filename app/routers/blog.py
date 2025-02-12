from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def myblog():
    return {"myblog": "testing my blog"}