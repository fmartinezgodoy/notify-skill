---
name: task-notify
description: Notify user via smart speaker when requested
---

# Task Notify Skill

Use this skill when the user asks you to notify them when a task is complete (e.g., "let me know when you're done", "notify me when finished").

## How to notify

Use the IoT Gateway MCP `control_devices` tool:

```
device_id: cast_192.168.68.56
action: speak  
params: { "message": "YOUR_MESSAGE" }
```

## Message format
Summarize what was completed:
- "Code changes committed and pushed"
- "Tests passed, deployment complete"
- "Feature implementation finished"

## Devices
- `cast_192.168.68.56` - Living room
- `cast_192.168.68.61` - Estudio
