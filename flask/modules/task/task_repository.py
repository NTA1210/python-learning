from sqlalchemy.orm import Session
from modules.task.task_model import Task
from datetime import datetime


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, name:str, startTime:datetime, endTime:datetime) -> Task:
        task = Task(name=name, startTime=startTime, endTime=endTime)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task
    
    def get_all(self):
        return self.db.query(Task).all()