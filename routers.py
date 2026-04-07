from fastapi import APIRouter, Depends
from services import get_all_tasks, user_creates_task, get_task_by_id, update_task, delete_task
from schemas import Task, TaskResponse
from database import SessionLocal
from sqlalchemy.orm import Session


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return get_all_tasks(db)


@router.post("/createTasks", response_model=TaskResponse)
def create_task(task: Task, db: Session = Depends(get_db)):
    return user_creates_task(task, db)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task_withID(task_id: int, db: Session = Depends(get_db)):
    return get_task_by_id(task_id, db)


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task_info(task_id: int, updated_task: Task, db: Session = Depends(get_db)):
    return update_task(task_id, updated_task, db)


@router.delete("/tasks/{task_id}", response_model=TaskResponse)
def delete_task_from_list(task_id: int, db: Session = Depends(get_db)):
    return delete_task(task_id, db)