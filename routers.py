from fastapi import APIRouter
from services import get_all_tasks, user_creates_task, get_task_by_id, update_task, delete_task
from models import Task, TaskResponse


router = APIRouter()


@router.get("/tasks")
def get_tasks():
    return get_all_tasks()


@router.post("/createTasks", response_model=TaskResponse)
def create_task(task: Task):
    return user_creates_task(task)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task_withID(task_id: int):
    return get_task_by_id(task_id)


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task_info(task_id: int, updated_task: Task):
    return update_task(task_id, updated_task)


@router.delete("/tasks/{task_id}", response_model=TaskResponse)
def delete_task_from_list(task_id: int):
    return delete_task(task_id)