# Notify Skill

A cross-tool compatible skill that sends audio notifications to your smart speakers when AI tasks complete.

## What it does

Sends a text-to-speech message to your Google Nest/Home speakers via your Home IoT Gateway.

## Usage

After completing a task, call the notify endpoint to announce completion:

```bash
curl -X POST http://YOUR_GATEWAY_IP:8080/api/v1/notify \
  -H "Content-Type: application/json" \
  -d '{"message": "Task completed successfully"}'
```

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `message` | Yes | The message to speak |
| `device_id` | No | Target speaker ID (defaults to living room) |

## Examples

### Simple notification
```bash
curl -X POST http://rpi:8080/api/v1/notify \
  -H "Content-Type: application/json" \
  -d '{"message": "Your code has been deployed"}'
```

### Specify device
```bash
curl -X POST http://rpi:8080/api/v1/notify \
  -H "Content-Type: application/json" \
  -d '{"message": "Build complete", "device_id": "cast_192.168.68.61"}'
```

### Using the shell script
```bash
./notify.sh "Task completed successfully"
```

## Setup

1. Ensure your Home IoT Gateway is running
2. Set the `IOT_GATEWAY_URL` environment variable:
   ```bash
   export IOT_GATEWAY_URL="http://rpi:8080"
   ```

## Device IDs

Discover available speakers:
```bash
curl -s http://rpi:8080/api/v1/devices | grep -o '"id":"cast_[^"]*"'
```

Common device IDs:
- `cast_192.168.68.56` - Living room Nest Audio
- `cast_192.168.68.61` - Estudio Nest Mini
