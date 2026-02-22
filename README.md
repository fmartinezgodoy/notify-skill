# Notify Skill

A cross-tool compatible skill that sends audio notifications to Google Nest/Home speakers when AI coding tasks complete.

## Compatible With

- **Factory/Droid** - Install as a custom droid
- **Claude Code** - Use the shell script or read SKILL.md
- **Codex** - Use the shell script or Python helper
- **Any AI tool** - Just call the HTTP endpoint

## Quick Start

```bash
# Set your gateway URL
export IOT_GATEWAY_URL="http://rpi:8080"

# Send a notification
./notify.sh "Task completed successfully"
```

## Installation

### For Factory/Droid

Copy `task-notify.md` to your droids directory:

```bash
mkdir -p ~/.factory/droids
cp task-notify.md ~/.factory/droids/task-notify.md
```

### For other tools

Source the shell script or use the Python helper directly.

## API Endpoint

```
POST /api/v1/notify
Content-Type: application/json

{
  "message": "Your message here",
  "device_id": "cast_192.168.68.56"  // optional
}
```

## Requirements

- Home IoT Gateway running on your network
- Google Nest/Home speakers configured
- Network access to the gateway
