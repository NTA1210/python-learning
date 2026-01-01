from database import SessionLocal
from modules.task.task_repository import TaskRepository

class TaskService:

    @staticmethod
    def create(data):
        db = SessionLocal()
        try:
            repo = TaskRepository(db)
            return repo.create(data['name'], data['startTime'], data['endTime'])
        finally:
            db.close()

    @staticmethod
    def get_all():
        db = SessionLocal()
        try:
            repo = TaskRepository(db)
            return repo.get_all()
        finally:
            db.close()