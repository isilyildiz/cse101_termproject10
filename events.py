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
    events.append(event_data)
    return event_data
