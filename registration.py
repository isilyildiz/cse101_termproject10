
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


#(week3)
def create_registration(registrations: list, data: dict, events: list) -> dict:
    event_id = data["event_id"]

    # Find event
    event = None
    for e in events:
        if e["id"] == event_id:
            event = e
            break

    if event is None:
        raise ValueError("Event not found")

    # Count confirmed registrations
    confirmed_regs = [
        r for r in registrations
        if r["event_id"] == event_id and r["status"] == "confirmed"
    ]

    if len(confirmed_regs) < event["capacity"]:
        status = "confirmed"
        seat_number = len(confirmed_regs) + 1
    else:
        status = "waitlist"
        seat_number = None

    reg = {
        "id": str(uuid.uuid4()),
        "attendee_id": data["attendee_id"],
        "event_id": event_id,
        "timestamp": datetime.now().isoformat(),
        "confirmation_code": str(uuid.uuid4())[:8],
        "seat_number": seat_number,
        "status": status,
        "payment_status": "paid"
    }

    registrations.append(reg)
    return reg

#(week3)
def promote_waitlist(registrations: list, event_id: str):
    waitlist = [
        r for r in registrations
        if r["event_id"] == event_id and r["status"] == "waitlist"
    ]

    if not waitlist:
        return None

    confirmed_count = len([
        r for r in registrations
        if r["event_id"] == event_id and r["status"] == "confirmed"
    ])

    reg = waitlist[0]
    reg["status"] = "confirmed"
    reg["seat_number"] = confirmed_count + 1
    return reg


def cancel_registration(registrations: list, registration_id: str, events: list):
    for r in registrations:
        if r["id"] == registration_id:
            r["status"] = "cancelled"
            r["seat_number"] = None

            promote_waitlist(registrations, r["event_id"])
            return r

    return None


def calculate_event_revenue(registrations: list, event_id: str, events: list) -> float:
    event = None
    for e in events:
        if e["id"] == event_id:
            event = e
            break

    if event is None:
        return 0.0

    total = 0.0
    for r in registrations:
        if (
            r["event_id"] == event_id and
            r["status"] == "confirmed" and
            r["payment_status"] == "paid"
        ):
            total += event["price"]

    return total
