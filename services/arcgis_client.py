import httpx
import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent)) 
from config import settings
from models.search_response import SearchResponse
from models.feature_query_response import QueryResponse
from models.fields import Field
from models.feature import Feature
from models.portal_item import PortalItem
class ArcGISClient:
    def __init__(self):
        self.portal_url = str(settings.arcgis_portal_url).rstrip("/")
        #self.session = httpx.AsyncClient(base_url=self.portal_url)
    
    @property
    def search_url(self) -> str:
        return f"{self.portal_url}/sharing/rest/search"
    def feature_layer_url(self, layer_url: str) -> str:
        return f"{layer_url}/query"


    async def search_items(self, query: str):
        params = {
            "q": query,
            "f": "json"
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(
                self.search_url,
                params=params
            )
            response.raise_for_status() # Raise an exception for bad status codes 404, 500, etc.
            print("Request URL:", response.request.url)
            print("Response URL:", response.url)
            return response.json()

    def parse_search_response(
        self,
        data: dict
    ) -> SearchResponse:

        items = []
        for item in data["results"]:
            items.append(
                PortalItem(
                    id=item["id"],
                    title=item["title"],
                    type=item["type"],
                    owner=item["owner"],
                    snippet=item.get("snippet"),
                    tags=item.get("tags", []),
                    url=item.get("url"),
                    created=item.get("created"),
                    modified=item.get("modified"),
                    descibtion=item.get("description")
                )
            )
        return SearchResponse(
            total=data["total"],
            start=data["start"],
            num=data["num"],
            items=items
        )
    
    
    async def query_feature_layer(
        self,
        layer_url: str,
        query: dict
    ):
        if "f" not in query:
            query["f"] = "json"
        async with httpx.AsyncClient() as client:
            response = await client.get(
                self.feature_layer_url(layer_url),
                params=query
            )
            response.raise_for_status() # Raise an exception for bad status codes 404, 500, etc.
            print("Request URL:", response.request.url)
            print("Response URL:", response.url)
            return response.json()


    def parse_query_response(
        self,
        data: dict
    ) -> QueryResponse:
        fields = []
        for field in data["fields"]:
            fields.append(
                Field(
                    name=field["name"],
                    type=field["type"],
                    alias=field.get("alias")
                )
            )
        features =[
            Feature(
                attributes=feature.get("attributes",{}),
                geometry=feature.get("geometry")
            )
            for feature in data.get("features", [])
        ]  

        return QueryResponse(
            features=features,
            fields=fields,
            geometry_type=data.get("geometryType")
        )

if __name__ == "__main__":
    import asyncio
    async def main():
        client = ArcGISClient()
        result = await client.query_feature_layer(
            "https://services5.arcgis.com/jKr2AYWt9jphbXiT/arcgis/rest/services/Centers_loactions/FeatureServer/0",
            {"where": "1=1", "outFields": "*","limit": 10, "f": "json"}
        )
        #print(result)
        parsed = client.parse_query_response(result)
        print(parsed)
    asyncio.run(main())