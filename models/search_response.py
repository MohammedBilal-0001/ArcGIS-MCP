from pydantic import BaseModel

from models.portal_item import PortalItem

class SearchResponse(BaseModel):
    total: int
    start: int
    num: int

    items: list[PortalItem]