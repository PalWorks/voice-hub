# Voice Hub

Voice Hub orchestrates multiple Model Context Protocol (MCP) agents.  
This repository ships only thin glue code and tracks the MCP agents as git
submodules under `external/`.

## Repository Layout

```
voice-hub/
├── external/             # MCP agents (git submodules)
│   ├── OpenHands/
│   └── Gmail-MCP-Server/
├── src/
│   ├── glue/             # Webhook server and OpenHands client
│   └── config/           # Sample configuration files
├── scripts/              # Helper scripts
├── docker-compose.yml    # Multi-service deployment
└── .env.example          # Sample environment variables
```

## Getting Started

1. **Clone and init submodules**

```bash
git clone <this-repo>
cd voice-hub
git submodule update --init --recursive
```

2. **Configure environment variables**

Copy `.env.example` to `.env` and adjust values as needed. The glue service
uses `WEBHOOK_SECRET` for webhook verification and `OPENHANDS_API` to send
requests to OpenHands.

3. **Build and run**

```
docker compose up --build
```

This will build OpenHands, Gmail MCP and the glue service. The default exposed
ports are:

- OpenHands: `8000`
- Gmail MCP: `8001`
- Glue server: `8080`

Update `PORT_*` variables in `.env` to change mappings.

## ElevenLabs Integration

Configure ElevenLabs (or any other webhook sender) to POST JSON payloads to
`http://<your-host>:8080/webhook` with the header `X-Webhook-Secret` matching
your `WEBHOOK_SECRET` value.

## Adding New MCPs

1. Add the MCP repository as a submodule inside `external/`:

```bash
git submodule add <repo-url> external/<folder-name>
```

2. Create a new service section in `docker-compose.yml` following the existing
examples and assign it a unique port.

3. Update `.env.example` with the new port and any additional configuration.

Commit the updated `.gitmodules`, `docker-compose.yml` and `.env.example`.
