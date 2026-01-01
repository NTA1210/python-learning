from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    startTime = Column(DateTime(timezone=True), nullable=False)
    endTime = Column(DateTime(timezone=True), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "startTime": self.startTime,
            "endTime": self.endTime}