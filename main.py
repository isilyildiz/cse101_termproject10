from events import load_events, save_events, create_event

DATA_PATH = "data/events.json"

def main():
    events = load_events(DATA_PATH)
    print("Kayıtlı etkinlik sayısı:", len(events))

    new_event = {
        "id": "U001",
        "name": "GDG club 2025",
        "location": "Istanbul",
        "start_date": "2025-05-01",
        "end_date": "2025-05-03",
        "capacity": 200,
        "price": 150,
        "description": "A tech conference",
        "sessions": []
    }

    create_event(events, new_event)

    save_events(DATA_PATH, events)

    print("Yeni etkinlik eklendi!")
    print("Güncel etkinlik sayısı:", len(events))

if __name__ == "__main__":
    main()
