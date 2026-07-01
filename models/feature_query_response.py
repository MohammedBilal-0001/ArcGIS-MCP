from pydantic import BaseModel
from typing import List
from .feature import Feature
from .fields import Field

class QueryResponse(BaseModel):
    features: List[Feature]
    fields: List[Field]
    geometry_type: str | None = None