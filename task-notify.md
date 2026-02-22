You are a notification skill. After completing any significant task, notify the user via their smart speaker.

## When to use
Call this skill after completing a significant task (code written, tests passed, deployment done, etc.)

## How to notify

Use the Execute tool to call the commands API:

```bash
curl -X POST http://rpi:8080/api/v1/commands \
  -H "Content-Type: application/json" \
  -d '{"commands":[{"device_id":"cast_192.168.68.56","action":"speak","params":{"message":"YOUR_MESSAGE"}}]}'
```

Replace `YOUR_MESSAGE` with a description of what was completed.

## Example messages

- "Code changes committed and pushed"
- "Tests passed successfully"  
- "Deployment complete"
- "Pull request created"
- "Feature implementation finished"

## Device options

Change `device_id` for different speakers:
- `cast_192.168.68.56` - Living room (default)
- `cast_192.168.68.61` - Estudio

## MCP Alternative

If MCP is available, you can also use the `control_devices` tool with the same parameters.
