# Voice AI MCP Stack (Starter)

This project sets up a microservices stack for a voice-first AI assistant using Docker Compose.  
**Initial version**: Caddy reverse proxy + FastAPI hello world webhook.

---

## Quickstart

### 1. Prerequisites

- Docker & Docker Compose installed
- (Production) Domain with Cloudflare DNS (see instructions below)

### 2. Clone & Run

```bash
git clone https://github.com/YOURNAME/voice-ai-mcp-stack.git
cd voice-ai-mcp-stack
cp .env.example .env   # (Add env vars as needed)
docker compose up --build -d
