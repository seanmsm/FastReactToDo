from typing import List, Dict

from fastapi import APIRouter, HTTPException
from backend.apps.todo.models.task_model import TaskModel, TaskDataModel

todos: Dict[int, TaskModel] = {
    1: TaskModel(id=1, desc='task 1', tags=['tag1', 'tag2'], completed=False),
    2: TaskModel(id=2, desc='task 2', tags=['tag2', 'tag3'], completed=True)
}

todo_router = APIRouter()


@todo_router.get("/", response_description="List all tasks")
async def get_todos() -> List[TaskModel]:
    return list(todos.values())


@todo_router.get("/{id}", response_description="Get a single task")
async def get_todo(task_id: int) -> TaskModel:
    task = todos.get(task_id, None)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

    return task


@todo_router.post("/", response_description="Add new task", status_code=201)
async def create_task(task_data: TaskDataModel) -> TaskModel:
    used_ids = todos.keys()
    new_id = [*(set(range(1, max(used_ids) + 2)) - set(used_ids))][0]
    new_task = TaskModel(id=new_id, **task_data.dict())
    todos[new_id] = new_task
    return new_task


@todo_router.put("/{id}", response_description="Update a task")
async def update_task(task_id: int, task_data: TaskDataModel) -> TaskModel:
    task = todos.get(task_id, None)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

    todos[task_id].desc = task_data.desc
    todos[task_id].tags = task_data.tags
    todos[task_id].completed = task_data.completed
    return todos[task_id]


@todo_router.delete("/{id}", response_description="Delete a task", status_code=204)
async def remove_task(task_id: int) -> None:
    task = todos.get(task_id, None)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

    todos.pop(task_id)
