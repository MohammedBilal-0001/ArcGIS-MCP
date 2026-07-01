from pydantic import BaseModel
from typing import Dict, Any

class Feature(BaseModel):

    attributes: Dict[str, Any]
    geometry: Dict[str, Any] | None = None
