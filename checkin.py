from datetime import datetime
import os


def check_in_attendee(registrations: list, registration_id: str) -> dict:
    for r in registrations:
        if r["id"] == registration_id:
            if r.get("checked_in"):
                return r  # already checked in

            if r["status"] != "confirmed":
                raise ValueError("Only confirmed registrations can be checked in")

            r["checked_in"] = True
            r["checked_in_at"] = datetime.now().isoformat()
            return r

    raise ValueError("Registration not found")


def list_checked_in_attendees(registrations: list, event_id: str) -> list:
    return [
        r for r in registrations
        if r["event_id"] == event_id and r.get("checked_in")
    ]


def generate_badge(attendee: dict, registration: dict, directory: str) -> str:
    os.makedirs(directory, exist_ok=True)

    filename = f"badge_{registration['id']}.txt"
    path = os.path.join(directory, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write("=== EVENT BADGE ===\n")
        f.write(f"Name: {attendee['name']}\n")
        f.write(f"Event ID: {registration['event_id']}\n")
        f.write(f"Seat: {registration.get('seat_number', 'N/A')}\n")
        f.write(f"Ticket Type: {attendee.get('ticket_type', 'General')}\n")

    return path


def session_attendance(registrations: list, event_id: str, session_id: str) -> dict:
    total = 0
    checked_in = 0

    for r in registrations:
        if r["event_id"] == event_id:
            total += 1
            if r.get("checked_in"):
                checked_in += 1

    return {
        "session_id": session_id,
        "registered": total,
        "checked_in": checked_in
    }