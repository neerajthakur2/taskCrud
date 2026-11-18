from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.tasks.dtos import TaskSchema
from src.tasks.models import TaskModel


def create_task(body: TaskSchema, db: Session) -> TaskModel:
    new_task = TaskModel(**body.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_tasks(db: Session):
    tasks = db.query(TaskModel).all()
    return {"status": "all tasks", "data": tasks}


def get_one_task(task_id: int, db: Session) -> TaskModel:
    one_task = db.get(TaskModel, task_id)
    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return one_task


def update_task(task_id: int, body: TaskSchema, db: Session) -> TaskModel:
    task_to_update = db.get(TaskModel, task_id)
    if not task_to_update:
        raise HTTPException(status_code=404, detail="Task not found")
# update
    update_data = body.model_dump()
    for key, value in update_data.items():
        setattr(task_to_update, key, value)

    db.commit()
    db.refresh(task_to_update)
    return task_to_update



# delete task

def delete_task(task_id:int,db:Session):
    one_task = db.get(TaskModel, task_id)
    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(one_task)
    db.commit()
    return {
        "status":"task deleted successfully"
    }
