from models import TaskResponse, Task
from fastapi import HTTPException


# Create a task

task_db = []

def user_creates_task(task: Task):
    new_task = TaskResponse(
        id=len(task_db) + 1,
        title=task.title,
        description=task.description,
        completed=task.completed
    )
    task_db.append(new_task)
    return new_task


def get_all_tasks():
    return task_db


def get_task_by_id(task_id: int):
    for task in task_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


def update_task(task_id: int, updated_task: Task):
    for task in task_db:
        if task.id == task_id:
            # Update the task with the new information
            task.title = updated_task.title
            task.description = updated_task.description
            task.completed = updated_task.completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")


def delete_task(task_id: int):
    for task in task_db:
        if task.id == task_id:
            task_db.remove(task)
            return task
    raise HTTPException(status_code=404, detail="Task not found")

