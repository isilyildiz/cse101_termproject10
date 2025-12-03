import json
import uuid


def load_attendees(path: str) -> list:
    """Load attendee list from JSON file."""
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_attendees(path: str, attendees: list) -> None:
    """Save attendee list to JSON file."""
    with open(path, "w") as f:
        json.dump(attendees, f)


def register_attendee(attendees: list, profile: dict) -> dict:
    """Create a new attendee profile."""
    attendee = {
        "id": str(uuid.uuid4()),
        "name": profile["name"],
        "email": profile["email"],
        "pin": str(profile.get("pin", "0000")),
        "organization": profile.get("organization", ""),
        "dietary": profile.get("dietary", ""),
        "ticket_type": profile.get("ticket_type", "General")
    }

    attendees.append(attendee)
    return attendee


def authenticate_attendee(attendees: list, email: str, pin: str):
    """Return attendee if credentials are correct."""
    for att in attendees:
        if att["email"] == email and att["pin"] == pin:
            return att
    return None


def update_attendee(attendees: list, attendee_id: str, updates: dict):
    """Update attendee info."""
    for att in attendees:
        if att["id"] == attendee_id:
            att.update(updates)
            return att
    return None
