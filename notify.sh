#!/bin/bash
# Notify skill - sends TTS message to smart speakers
# Usage: notify.sh "Your message here" [device_id]

GATEWAY_URL="${IOT_GATEWAY_URL:-http://rpi:8080}"
MESSAGE="${1:-Task completed}"
DEVICE_ID="${2:-}"

if [ -n "$DEVICE_ID" ]; then
    curl -s -X POST "$GATEWAY_URL/api/v1/notify" \
        -H "Content-Type: application/json" \
        -d "{\"message\": \"$MESSAGE\", \"device_id\": \"$DEVICE_ID\"}"
else
    curl -s -X POST "$GATEWAY_URL/api/v1/notify" \
        -H "Content-Type: application/json" \
        -d "{\"message\": \"$MESSAGE\"}"
fi
