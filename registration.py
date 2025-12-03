
import json
import uuid
from datetime import datetime


def load_registrations(path: str) -> list:
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_registrations(path: str, registrations: list) -> None:
    with open(path, "w") as f:
        json.dump(registrations, f, indent=4)


def create_registration(registrations: list, data: dict, events: list) -> dict:
    """
    WEEK 2 — BASIC REGISTRATION
    ✔ attendee → event kayıt olur
    ✔ confirmation_code verilir
    ✔ timestamp eklenir
    ✔ seat_number basic olarak atanır
    ✘ capacity control (week 3)
    ✘ waitlist (week 3)
    ✘ cancellation (week 3)
    """

#FİNDİNG EVENT
    event_id = data["event_id"]
    event = None
    for e in events:
        if e["id"] == event_id:
            event = e

    if event is None:
        raise ValueError("Event not found")

    reg = {
        "id": str(uuid.uuid4()),
        "attendee_id": data["attendee_id"],
        "event_id": event_id,
        "timestamp": datetime.now().isoformat(),
        "confirmation_code": str(uuid.uuid4())[:8],
        "seat_number": len(registrations) + 1
    }

    registrations.append(reg)
    return reg
