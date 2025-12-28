from registration import create_registration, promote_waitlist

def test_capacity_and_waitlist():
    events = [{
        "id": "E001",
        "capacity": 1,
        "price": 100
    }]

    registrations = []

    r1 = create_registration(registrations, {
        "attendee_id": "A1",
        "event_id": "E001"
    }, events)

    r2 = create_registration(registrations, {
        "attendee_id": "A2",
        "event_id": "E001"
    }, events)

    assert r1["status"] == "confirmed"
    assert r2["status"] == "waitlist"


def test_waitlist_promotion():
    events = [{
        "id": "E001",
        "capacity": 1,
        "price": 100
    }]

    registrations = []

    create_registration(registrations, {
        "attendee_id": "A1",
        "event_id": "E001"
    }, events)

    create_registration(registrations, {
        "attendee_id": "A2",
        "event_id": "E001"
    }, events)

    promoted = promote_waitlist(registrations, "E001")
    assert promoted is not None
    assert promoted["status"] == "confirmed"
