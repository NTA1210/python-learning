from sqlalchemy.orm import Session
from modules.summary.summary_model import Summary


class SummaryRepository:
    def __init__(self, db : Session):
        self.db = db

    def summarize(self, filename:str) -> Summary:
        summary = Summary(filename=filename)
        self.db.add(summary)
        self.db.commit()
        self.db.refresh(summary)
        return summary