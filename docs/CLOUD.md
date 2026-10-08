# Cloud Deployment Notes (Phase 5)

## Recommended Free / Cheap Options

| Service     | Notes                                      | Difficulty |
|-------------|--------------------------------------------|------------|
| Render.com  | Easy for Python/Bash, free tier available  | Easy       |
| Railway.app | Simple deploy, free credits                | Easy       |
| Fly.io      | Good for always-on, free allowance         | Medium     |
| VPS (any)   | Full control, run bang.sh as a service     | Medium     |

## Basic Deploy Idea (Render / Railway)

1. Push this repo to GitHub (already done).
2. Create a new Web Service / Worker.
3. Build command: `pip install -r requirements.txt` (add one if needed).
4. Start command: `bash bang.sh` or a small wrapper that keeps it alive.
5. For always-on, use a process manager or the platform's worker type.

## Local Always-On Alternative

```bash
# Keep running with nohup
nohup ./bang.sh > bang.log 2>&1 &

# Or use screen/tmux
screen -S bang
./bang.sh
# Ctrl+A then D to detach
```

## Future

- Discord/Telegram bridge for playground mode
- Multiple instances of workers on different machines
- Shared memory via Redis or a simple API instead of local JSON
