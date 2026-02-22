#!/usr/bin/env python3
"""Notify skill - sends TTS message to smart speakers.

Usage:
    python notify.py "Your message here" [--device DEVICE_ID]
"""

import argparse
import json
import os
import urllib.request
from pathlib import Path

def load_config():
    """Load config from file or return defaults."""
    config_file = os.environ.get(
        "NOTIFY_CONFIG",
        str(Path.home() / ".config" / "notify-skill.json")
    )
    
    defaults = {
        "gateway_url": os.environ.get("IOT_GATEWAY_URL", "http://rpi:8080"),
        "default_device": "cast_192.168.68.56",
    }
    
    try:
        with open(config_file) as f:
            config = json.load(f)
            defaults.update(config)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    
    return defaults

def notify(message: str, device_id: str = None):
    """Send a notification to smart speakers."""
    config = load_config()
    
    gateway_url = config["gateway_url"]
    if device_id is None:
        device_id = config["default_device"]
    
    payload = {
        "commands": [{
            "device_id": device_id,
            "action": "speak",
            "params": {"message": message}
        }]
    }
    
    data = json.dumps(payload).encode("utf-8")
    
    req = urllib.request.Request(
        f"{gateway_url}/api/v1/commands",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result.get("results", [{}])[0].get("success", False)
    except Exception as e:
        print(f"Notification failed: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send notification to smart speakers")
    parser.add_argument("message", help="Message to speak")
    parser.add_argument("--device", "-d", help="Target device ID")
    
    args = parser.parse_args()
    
    success = notify(args.message, args.device)
    if success:
        print(f"Notification sent: {args.message}")
    else:
        print("Notification failed")
