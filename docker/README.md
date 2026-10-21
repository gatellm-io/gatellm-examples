# Docker Compose deployment

```bash
cp .env.docker.example .env
# edit .env: replace all three placeholder values
docker compose up -d
```

The console is then at <http://localhost:7890>. Port 7890 is bound to `127.0.0.1` only —
put a reverse proxy in front of it before exposing the gateway to other machines.

The values:

| Variable | What it is |
|---|---|
| `CONSOLE_PASSWORD` | First-login password for the admin console. Change it after the first login. |
| `ENCRYPTION_KEY` | Encrypts the upstream provider keys you store in the console. Everything must use the same key, or the stored keys cannot be decrypted. |
| `CONSOLE_SECRET_KEY` | Signs console sessions. |
| `STORAGE_MODE` | `sqlite` for a single node. Use the database-backed mode when you run more than one replica. |

Full walkthrough, including the Helm path: <https://docs.gatellm.io/en/quickstart/docker-single-node>.
