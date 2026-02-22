You are a notification skill. After completing any task, you should notify the user via their smart speaker.

## When to use
Call this skill after completing a significant task (code written, tests passed, deployment done, etc.)

## How to notify

Use the Execute tool to call the notify endpoint:

```bash
curl -X POST http://rpi:8080/api/v1/notify \
  -H "Content-Type: application/json" \
  -d '{"message": "TASK_DESCRIPTION completed"}'
```

## Example messages

- "Code changes committed and pushed"
- "Tests passed successfully"
- "Deployment complete"
- "Pull request created"
- "Feature implementation finished"

## Setup

Set environment variable if gateway is not at default location:
```bash
export IOT_GATEWAY_URL="http://YOUR_PI_IP:8080"
```

## Device options

Optional: specify a device_id for specific speakers:
- `cast_192.168.68.56` - Living room (default)
- `cast_192.168.68.61` - Estudio
