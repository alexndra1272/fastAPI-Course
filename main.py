from fastapi import FastAPI

app = FastAPI(title="MiniBlog")

POSTS = [
    {"id": 1, "title": "Flask", "content": "Is a microframework"},
    {"id": 2, "title": "Django", "content": "Is a framework"},
    {"id": 3, "title": "FastAPI", "content": "Is a nice framework for APIs"}
]

@app.get("/")
def index():
    return {"message": "This is my first endpoint using fastAPI - Cristel"}

@app.get("/posts")
def list_post():
    return {"data": POSTS}