# Notify Skill

A skill that lets AI assistants notify you via smart speaker when you ask them to.

## How it works

When you say things like:
- "Let me know when you're done"
- "Notify me when finished"
- "Tell me when complete"

The LLM reads this skill and uses the IoT Gateway MCP to send a TTS message to your speaker.

## Usage

Use the MCP `control_devices` tool:

```
device_id: cast_192.168.68.56
action: speak
params: { "message": "YOUR_MESSAGE" }
```

## Device IDs

- `cast_192.168.68.56` - Living room Nest Audio
- `cast_192.168.68.61` - Estudio Nest Mini

## Installation

```bash
# Clone the repo
git clone https://github.com/fmartinezgodoy/notify-skill.git

# Install for Factory/Droid
mkdir -p ~/.factory/droids
cp notify-skill/task-notify.md ~/.factory/droids/
```

## Requirements

- Home IoT Gateway running (https://github.com/fmartinezgodoy/home-iot-gateway)
- Google Nest/Home speakers configured
- MCP configured to point to your gateway
