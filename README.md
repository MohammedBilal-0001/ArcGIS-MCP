# ArcGIS MCP Server

A lightweight **Model Context Protocol (MCP)** server that connects Large Language Models (LLMs) to **ArcGIS REST APIs**.

This project demonstrates how an AI assistant can discover and retrieve ArcGIS content through MCP, providing a clean and extensible architecture that can later support authenticated ArcGIS Enterprise and ArcGIS Online deployments.

> **Status:** Prototype / Portfolio Project

---

## Features

- Search ArcGIS Portal content
- Query ArcGIS Feature Layers
- Modular architecture (Client → Builders → Models → MCP Tools)
- Typed models using Pydantic
- Built with the Anthropic MCP SDK

---

## Tech Stack

- Python 3.11+
- MCP SDK (`mcp` Python package)
- `httpx` for async HTTP calls
- `pydantic` + `pydantic-settings` for typed config and models
- ArcGIS REST API

---

## Architecture

This project is structured around a small, composable MCP server that exposes ArcGIS functionality as tools. High-level layers:

- Client: `services/arcgis_client.py` — thin HTTP client around the ArcGIS REST API using `httpx`.
- Builders: `services/query_builder.py` — helpers to construct ArcGIS search and query strings.
- Models: `models/` — typed `pydantic` models for responses and items.
- Tools: `tools/` — MCP tool functions wired into the MCP server in `server.py`.

Project layout:

```
arcgis-mcp/
├── models/          # Pydantic models
├── services/        # ArcGIS REST client + query builders
├── tools/           # MCP tools (search, query)
├── tests/           # Development scripts / tests
├── config.py        # Pydantic Settings-based config
├── server.py        # FastMCP server wiring
├── requirements.txt # Python dependencies
└── README.md
```

---

## Quick Start

### 1. Clone the repository

```bash
git clone <repository-url>
cd arcgis-mcp
```

### 2. Install dependencies

Create and activate a virtual environment, then install:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate     # Windows (PowerShell)
pip install -r requirements.txt
```

### 3. Configure the portal

Create a `.env` file:

```env
arcgis_portal_url=https://www.arcgis.com
```

Or provide the portal URL through your MCP client configuration.

### 4. Start the MCP server

Run the MCP server which registers the available tools and listens for MCP client connections:

```bash
python server.py
```

---

## Claude Desktop Example

```json
{
  "mcpServers": {
    "arcgis": {
            "command": "path\\to\\python.exe",
            "args": [
                "path\\to\\server.py"
            ],
            "env": {
                "arcgis_portal_url": "https://yourPortal.maps.arcgis.com",
                "orgid": "OrganizationId-to-limit-search"
            }
        }
}
```

---

## Screenshots

### Search and query Portal Content 

> ![Architecture](https://github.com/MohammedBilal-0001/ArcGIS-MCP/blob/main/Images/Screenshot%202026-06-19%20194949.png "searching portal and quering the feature layers")

---

### generate reports based on results

> ![Architecture](https://github.com/MohammedBilal-0001/ArcGIS-MCP/blob/main/Images/ArcGIS%20_mcp_test_1.png "Asking for fire risk analysis")

---

## Roadmap

- Authentication support
- Private ArcGIS Enterprise portals
- Additional ArcGIS REST tools
- Improved spatial query capabilities

---

## License

MIT
