from fastapi import FastAPI
import get
import post
import put
import delete

app = FastAPI()

app.include_router(get.router)
app.include_router(post.router)
app.include_router(put.router)
app.include_router(delete.router)