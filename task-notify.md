---
name: task-notify
description: Notify user via smart speaker when tasks complete
invocation:
  - when: always
    events:
      - stop
      - subagent_stop
---

# Task Notify Skill

After completing a significant task, notify the user via their smart speaker.

## How to notify

Use the IoT Gateway MCP to send a TTS message:

### Using MCP tool (preferred)
The IoT Gateway exposes an MCP server at `http://rpi:8080/mcp` with a `control_devices` tool.

Call it with:
```
device_id: cast_192.168.68.56
action: speak
params: { "message": "YOUR_MESSAGE_HERE" }
```

### Using HTTP API directly
```bash
curl -X POST http://rpi:8080/api/v1/commands \
  -H "Content-Type: application/json" \
  -d '{"commands":[{"device_id":"cast_192.168.68.56","action":"speak","params":{"message":"YOUR_MESSAGE"}}]}'
```

## When to notify
- After committing code
- After passing tests
- After deployment
- After creating a PR
- After completing a significant feature

## Message format
Be specific about what was completed:
- "Committed changes to authentication module"
- "All tests passed for user service"
- "Deployed version 1.2.0 to production"

## Device options
- `cast_192.168.68.56` - Living room (default)
- `cast_192.168.68.61` - Estudio
