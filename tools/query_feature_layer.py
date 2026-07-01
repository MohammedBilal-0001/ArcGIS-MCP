import sys
from pathlib import Path

import asyncio
# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))
from services.arcgis_client import ArcGISClient


async def query_feature_layer(
    layer_url: str,
    query: dict
):
    """
    Query a feature layer.
    
    Args:
        layer_url: The URL of the feature layer.
        query: The query to execute. as dict
    """
    client = ArcGISClient()
    result = await client.query_feature_layer(layer_url, query)
    return client.parse_query_response(result)


#     # test query layer from here
# if __name__ == "__main__":
#     import asyncio
#     result = asyncio.run(query_feature_layer("https://services5.arcgis.com/jKr2AYWt9jphbXiT/arcgis/rest/services/Centers_loactions/FeatureServer/0", {"where": "1=1","f": "json"}))
#     print(result)