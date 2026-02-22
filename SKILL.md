# Notify Skill

A cross-tool compatible skill that sends audio notifications to your Google Nest/Home speakers when AI tasks complete.

## What it does

Sends a text-to-speech message to your smart speakers using the existing IoT Gateway commands API.

## Usage

After completing a task, call the commands endpoint:

```bash
curl -X POST http://YOUR_PI:8080/api/v1/commands \
  -H "Content-Type: application/json" \
  -d '{"commands":[{"device_id":"cast_192.168.68.56","action":"speak","params":{"message":"YOUR_MESSAGE_HERE"}}]}'
```

## Configuration (optional)

Create `~/.config/notify-skill.json` for defaults:

```json
{
  "gateway_url": "http://rpi:8080",
  "default_device": "cast_192.168.68.56"
}
```

Then use the helper script:

```bash
./notify.sh "Task completed successfully"
```

## Device IDs

Discover available speakers:

```bash
curl -s http://rpi:8080/api/v1/devices/discover -X POST -H "Content-Type: application/json" -d '{"platform":"cast"}'
```

Common device IDs:
- `cast_192.168.68.56` - Living room Nest Audio  
- `cast_192.168.68.61` - Estudio Nest Mini

## MCP Alternative

If your tool supports MCP, you can also use the `control_devices` tool via the MCP endpoint at `/mcp`.
