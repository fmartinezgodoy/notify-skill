# Notify Skill

A cross-tool compatible skill with hooks for automatic notifications when AI tasks complete.

## Components

| File | Purpose |
|------|---------|
| `task-notify.md` | Skill instructions (for Droid/LLM to read) |
| `notify-on-stop.py` | Hook script (auto-runs on task completion) |
| `notify.sh` | Manual helper script |
| `notify.py` | Manual Python helper |

## Installation

### 1. Clone and setup
```bash
git clone https://github.com/fmartinezgodoy/notify-skill.git
cd notify-skill
```

### 2. Install for Factory/Droid
```bash
# Install skill
mkdir -p ~/.factory/droids
cp task-notify.md ~/.factory/droids/

# Install hook
mkdir -p ~/.factory/hooks
cp notify-on-stop.py ~/.factory/hooks/
chmod +x ~/.factory/hooks/notify-on-stop.py
```

### 3. Add hooks to settings
Add to `~/.factory/settings.json`:
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.factory/hooks/notify-on-stop.py"
          }
        ]
      }
    ],
    "SubagentStop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.factory/hooks/notify-on-stop.py"
          }
        ]
      }
    ]
  }
}
```

### 4. Configure (optional)
```bash
# Set environment variables
export IOT_GATEWAY_URL="http://rpi:8080"
export NOTIFY_DEVICE_ID="cast_192.168.68.56"
```

## How it works

1. **Skill** (`task-notify.md`) - Instructions for the LLM to follow
2. **Hook** (`notify-on-stop.py`) - Automatically triggers on Stop/SubagentStop events
3. **MCP** - The IoT Gateway exposes MCP tools at `/mcp`

## Manual usage
```bash
./notify.sh "Custom message"
```

## For other tools (Claude Code, Codex)
Use the HTTP API directly:
```bash
curl -X POST http://rpi:8080/api/v1/commands \
  -H "Content-Type: application/json" \
  -d '{"commands":[{"device_id":"cast_192.168.68.56","action":"speak","params":{"message":"Done"}}]}'
```
