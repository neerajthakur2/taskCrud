from pydantic import BaseModel

class TaskSchema(BaseModel,from_attributes=True):
      title: str
      description: str
      is_completed: bool=False