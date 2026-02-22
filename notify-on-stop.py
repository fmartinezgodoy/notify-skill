#!/usr/bin/env python3
"""
Hook that sends a notification when a task completes.
Runs on Stop and SubagentStop events.

Input (from stdin):
{
  "session_id": "...",
  "transcript_path": "...",
  "hook_event_name": "Stop" | "SubagentStop",
  "stop_hook_active": bool  # True if already in a stop hook loop
}
"""

import json
import sys
import urllib.request
import os

GATEWAY_URL = os.environ.get("IOT_GATEWAY_URL", "http://rpi:8080")
DEVICE_ID = os.environ.get("NOTIFY_DEVICE_ID", "cast_192.168.68.56")

def send_notification(message: str, device_id: str = None):
    """Send TTS notification to speaker."""
    if device_id is None:
        device_id = DEVICE_ID
    
    payload = {
        "commands": [{
            "device_id": device_id,
            "action": "speak",
            "params": {"message": message}
        }]
    }
    
    data = json.dumps(payload).encode("utf-8")
    
    req = urllib.request.Request(
        f"{GATEWAY_URL}/api/v1/commands",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return True
    except Exception as e:
        print(f"Notification failed: {e}", file=sys.stderr)
        return False

def main():
    # Read hook input
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)
    
    # Check if we're already in a stop hook loop (prevent infinite loops)
    if input_data.get("stop_hook_active", False):
        sys.exit(0)
    
    event = input_data.get("hook_event_name", "")
    
    # Different messages for different events
    if event == "SubagentStop":
        message = "Subtask completed"
    else:
        message = "Task completed"
    
    # Send notification
    send_notification(message)
    
    # Exit 0 = success, output goes to user in transcript mode
    sys.exit(0)

if __name__ == "__main__":
    main()
