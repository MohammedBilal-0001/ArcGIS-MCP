from pydantic import BaseModel

class Field(BaseModel):
    name: str
    type: str
    alias: str