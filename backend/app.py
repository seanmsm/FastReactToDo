from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.apps.todo.todo_router import todo_router

# TODO: meaningful tag descriptions
tags_metadata = [
    {
        "name": "root",
        "description": "TODO",
    },
    {
        "name": "tasks",
        "description": "TODO",
    }
]

app = FastAPI(openapi_tags=tags_metadata)
origins = ["http://localhost:3000", "localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(todo_router, tags=["tasks"], prefix="/task")


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "hello world"}
