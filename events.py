import json

def load_events(path: str) -> list:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_events(path: str, events: list) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(events, f, indent=4, ensure_ascii=False)

def create_event(events: list, event_data: dict) -> dict:
    if event_data["capacity"] <= 0:
        raise ValueError("Capacity must be greater than zero")

    events.append(event_data)
    return event_data


def update_event(events: list, event_id: str, updates: dict) -> dict:
    for event in events:
        if event["id"] == event_id:
            event.update(updates)
            return event
    return None

def add_session(events: list, event_id: str, session_data: dict) -> dict:
    for event in events:
        if event["id"] == event_id:
            event["sessions"].append(session_data)
            return session_data
    return None

def list_sessions(events: list, event_id: str) -> list:
    for event in events:
        if event["id"] == event_id:
            return event.get("sessions", [])
    return []


