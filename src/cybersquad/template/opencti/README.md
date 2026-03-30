# OpenCTI Homelab Stack for CyberSquad

This folder contains a local OpenCTI stack that matches the current CyberSquad OpenCTI prompt workflows and Ralph Loop backlog model.

## Scope

This stack is for local lab and learning use, not production.

## What is included

- `docker-compose.yml` with OpenCTI + worker + common import connectors
- `.env.example` with placeholder values only
- `.gitignore` that prevents local secrets from being committed

## Services

- Core: `opencti`, `worker`
- Data plane: `postgres`, `redis`, `rabbitmq`, `minio`, `elasticsearch`
- Connectors: MITRE, CISA KEV, URLhaus, AlienVault OTX

## Quick Start (Windows)

1. Create local data folders:

```powershell
New-Item -ItemType Directory -Force D:\opencti\data\redis | Out-Null
New-Item -ItemType Directory -Force D:\opencti\data\rabbitmq | Out-Null
New-Item -ItemType Directory -Force D:\opencti\data\postgres | Out-Null
New-Item -ItemType Directory -Force D:\opencti\data\minio | Out-Null
New-Item -ItemType Directory -Force D:\opencti\data\elasticsearch | Out-Null
```

2. Copy stack files:

```powershell
Copy-Item .\opencti\docker-compose.yml D:\opencti\docker-compose.yml -Force
Copy-Item .\opencti\.env.example D:\opencti\.env -Force
```

3. Edit `D:\opencti\.env` and replace every `CHANGE_ME_*` value.

4. Start the stack:

```powershell
cd D:\opencti
docker compose up -d
```

5. Check startup logs:

```powershell
docker compose logs -f opencti
```

## Endpoints

- OpenCTI: <http://localhost:8080>
- RabbitMQ UI: <http://localhost:15672>
- MinIO Console: <http://localhost:9001>
- Elasticsearch: <http://localhost:9200>

## Security Notes

- Never commit `.env`.
- Use one technical OpenCTI account/API token for automation at homelab stage.
- Keep personas as workflow owners in prompts/PRD; do not create one OpenCTI user per persona unless you need strict audit separation.
