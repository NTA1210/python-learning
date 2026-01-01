from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base

class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.filename,
            "created_at": self.created_at
        }