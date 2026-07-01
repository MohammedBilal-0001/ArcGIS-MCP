import asyncio
import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from services.arcgis_client import ArcGISClient
from services.query_builder import SearchQueryBuilder
async def main():
    client = ArcGISClient()
    q = SearchQueryBuilder.build(
    query= "latakia",
    owner="hisemdar",
    item_type="Map",
    num=2
)
    result = await client.search_items(q)
    #print(result)
    parsed = client.parse_search_response(result)
    print(parsed)
    print(client.portal_url)

if __name__ == "__main__":
    asyncio.run(main())
