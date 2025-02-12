from fastapi import FastAPI
from app.routers import blog, poll

app = FastAPI()

@app.get("/")
async def root():
    return {"my app": "testing my fastapi"}

app.include_router(blog.router, prefix="/blog")
app.include_router(poll.router, prefix="/poll")
