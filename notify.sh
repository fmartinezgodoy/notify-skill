#!/bin/bash
# Notify skill - sends TTS message to smart speakers
# Usage: notify.sh "Your message here" [device_id]

# Config file location
CONFIG_FILE="${NOTIFY_CONFIG:-$HOME/.config/notify-skill.json}"

# Read config or use defaults
if [ -f "$CONFIG_FILE" ]; then
    GATEWAY_URL=$(grep -o '"gateway_url"[[:space:]]*:[[:space:]]*"[^"]*"' "$CONFIG_FILE" | cut -d'"' -f4)
    DEFAULT_DEVICE=$(grep -o '"default_device"[[:space:]]*:[[:space:]]*"[^"]*"' "$CONFIG_FILE" | cut -d'"' -f4)
fi

GATEWAY_URL="${GATEWAY_URL:-${IOT_GATEWAY_URL:-http://rpi:8080}}"
DEFAULT_DEVICE="${DEFAULT_DEVICE:-cast_192.168.68.56}"

MESSAGE="${1:-Task completed}"
DEVICE_ID="${2:-$DEFAULT_DEVICE}"

curl -s -X POST "$GATEWAY_URL/api/v1/commands" \
    -H "Content-Type: application/json" \
    -d "{\"commands\":[{\"device_id\":\"$DEVICE_ID\",\"action\":\"speak\",\"params\":{\"message\":\"$MESSAGE\"}}]}"
