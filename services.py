from schemas import TaskResponse, Task
from fastapi import HTTPException
from models import TaskDB
from sqlalchemy.orm import Session


# Create a task



def user_creates_task(task: Task, db):
    new_task = TaskDB(
        title=task.title,
        description=task.description,
        completed=task.completed
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
    
   

def get_all_tasks(db):
    return db.query(TaskDB).all()


def get_task_by_id(task_id: int, db:Session):
    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


def update_task(task_id: int, updated_task: Task, db: Session):
    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    # Update the task with the new information
    task.title = updated_task.title
    task.description = updated_task.description
    task.completed = updated_task.completed
    db.commit()
    db.refresh(task)
    return task
    


def delete_task(task_id: int, db: Session):
    task=db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return task

    
