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
- Anthropic MCP SDK
- HTTPX
- Pydantic
- ArcGIS REST API

---

## Project Structure

```
arcgis-mcp/
│
├── models/          # Pydantic models
├── services/        # ArcGIS REST client
├── builders/        # Query builders
├── tools/           # MCP tools
├── tests/           # Development tests
├── config.py
├── server.py
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

```bash
pip install -r requirements.txt
```

### 3. Configure the portal

Create a `.env` file:

```env
arcgis_portal_url=https://www.arcgis.com
```

Or provide the portal URL through your MCP client configuration.

### 4. Start the MCP server

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

### Search Portal Content

> *(Add screenshot here)*

---

### Query Feature Layer

> *(Add screenshot here)*

---

## Roadmap

- Authentication support
- Private ArcGIS Enterprise portals
- Additional ArcGIS REST tools
- Improved spatial query capabilities

---

## License

MIT
