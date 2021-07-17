import pytest

import backend.apps.todo.todo_router as todo_router
from backend.apps.todo.models.task_model import TaskModel, TaskDataModel


@pytest.fixture
def new_data():
    desc = 'task new'
    tags = ['tag1 new', 'tag2 new']
    completed = True

    return TaskDataModel(desc=desc, tags=tags, completed=completed)


@pytest.mark.asyncio
async def test_get_todos():
    expected = [TaskModel(id=1, desc='task 1', tags=['tag1', 'tag2'], completed=False),
                TaskModel(id=2, desc='task 2', tags=['tag2', 'tag3'], completed=True)]
    result = await todo_router.get_todos()
    assert expected == result


@pytest.mark.asyncio
async def test_get_todo():
    expected = TaskModel(id=1, desc='task 1', tags=['tag1', 'tag2'], completed=False)
    result = await todo_router.get_todo(1)
    assert expected == result


@pytest.mark.asyncio
async def test_create_task(new_data):
    expected = TaskModel(id=3, desc=new_data.desc, tags=new_data.tags, completed=new_data.completed)

    task_data = new_data
    result = await todo_router.create_task(task_data)

    assert expected == result


@pytest.mark.asyncio
async def test_update_task(new_data):
    task_id = 1
    expected = TaskModel(id=task_id, desc=new_data.desc, tags=new_data.tags, completed=new_data.completed)

    task_data = new_data
    result = await todo_router.update_task(task_id, task_data)

    assert expected == result


@pytest.mark.asyncio
async def test_remove_task(new_data):
    task_id = 1
    expected = [TaskModel(id=2, desc='task 2', tags=['tag2', 'tag3'], completed=True),
                TaskModel(id=3, desc=new_data.desc, tags=new_data.tags, completed=new_data.completed)]

    await todo_router.remove_task(task_id)

    result = await todo_router.get_todos()

    assert expected == result
