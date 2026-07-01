from pydantic import BaseModel

class PortalItem(BaseModel):
    id: str
    title: str
    owner: str
    type: str
    
    snippet: str | None = None
    descibtion: str | None = None
    tags: list[str] = []
    url: str | None = None
    created: int | None = None
    modified: int | None = None