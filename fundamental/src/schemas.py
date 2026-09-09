from pydantic import BaseModel
from datetime import datetime
class PostCreate(BaseModel):
    title: str 
    content: str
    published: datetime  = datetime.now()
