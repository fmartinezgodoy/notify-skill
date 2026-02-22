# Notify Skill

A simple skill that lets AI assistants notify you via smart speaker when you ask them to.

## How it works

When you say things like:
- "Let me know when you're done"
- "Notify me when finished"  
- "Tell me when complete"

The LLM reads this skill and knows to use your IoT Gateway's MCP to send a TTS message to your speaker.

## Installation

```bash
# Clone the repo
git clone https://github.com/fmartinezgodoy/notify-skill.git

# Install for Factory/Droid
mkdir -p ~/.factory/droids
cp notify-skill/task-notify.md ~/.factory/droids/
```

## Usage

Just ask your AI:
> "Implement feature X and let me know when you're done"

The AI will:
1. Complete the task
2. Call the MCP `control_devices` tool
3. Your speaker announces completion

## Requirements

- Home IoT Gateway running (https://github.com/fmartinezgodoy/home-iot-gateway)
- Google Nest/Home speakers configured
- MCP configured to point to your gateway
