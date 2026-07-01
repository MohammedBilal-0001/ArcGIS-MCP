import sys
from pathlib import Path

import asyncio
# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))
from services.arcgis_client import ArcGISClient
from services.query_builder import SearchQueryBuilder
from config import settings



async def search_portal_content(
    query: str,
    owner: str | None= None,
    item_type: str | None= None,
    num: int | None= None,
    myOrgOnly: bool | None= None
):
    """Search ArcGIS Portal content.

    Searches the configured ArcGIS Portal for items
    matching the provided query and optional filters.

    Args:
        query: Search text.
        owner: Restrict results to an owner.
        myOrgOnly: Restrict results to your organization only.
        item_type: Restrict results by ArcGIS item type."""
    client = ArcGISClient()
    q = SearchQueryBuilder.build(
        query=query,
        owner=owner,
        item_type=item_type,
        num=num,
        orgid=settings.orgid if myOrgOnly else None
    )
    result = await client.search_items(q)
    parsed = client.parse_search_response(result)
    #print(parsed)
    return parsed.model_dump()

# if __name__ == "__main__":
#     result = asyncio.run(search_portal_content(
#         query="malibu",
#         #owner="hisemdar",
#         myOrgOnly=True
#     ))
#     print(result)
