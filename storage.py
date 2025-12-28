import json
import os
import shutil
from datetime import datetime


def load_state(base_dir: str):
    with open(os.path.join(base_dir, "events.json"), "r", encoding="utf-8") as f:
        events = json.load(f)

    with open(os.path.join(base_dir, "attendees.json"), "r", encoding="utf-8") as f:
        attendees = json.load(f)

    with open(os.path.join(base_dir, "registrations.json"), "r", encoding="utf-8") as f:
        registrations = json.load(f)

    return events, attendees, registrations


def save_state(base_dir: str, events: list, attendees: list, registrations: list) -> None:
    with open(os.path.join(base_dir, "events.json"), "w", encoding="utf-8") as f:
        json.dump(events, f, indent=4, ensure_ascii=False)

    with open(os.path.join(base_dir, "attendees.json"), "w", encoding="utf-8") as f:
        json.dump(attendees, f, indent=4, ensure_ascii=False)

    with open(os.path.join(base_dir, "registrations.json"), "w", encoding="utf-8") as f:
        json.dump(registrations, f, indent=4, ensure_ascii=False)


def backup_state(base_dir: str, backup_dir: str) -> list[str]:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, timestamp)
    os.makedirs(backup_path, exist_ok=True)

    files = ["events.json", "attendees.json", "registrations.json"]
    backed_up = []

    for file in files:
        src = os.path.join(base_dir, file)
        dst = os.path.join(backup_path, file)
        shutil.copy(src, dst)
        backed_up.append(dst)

    return backed_up


def validate_registration(registration: dict) -> bool:
    required_fields = ["id", "event_id", "attendee_id", "status"]

    for field in required_fields:
        if field not in registration:
            return False

    return True
