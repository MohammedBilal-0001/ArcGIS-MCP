from mcp.server.fastmcp import FastMCP
from tools.search_portal_content import search_portal_content
from tools.query_feature_layer import query_feature_layer
mcp = FastMCP("arcgis-mcp")
mcp.tool()(search_portal_content)
mcp.tool()(query_feature_layer)

if __name__ == "__main__":

    mcp.run()