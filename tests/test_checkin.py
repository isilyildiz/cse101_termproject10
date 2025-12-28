import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from checkin import check_in_attendee

def test_checkin_sets_timestamp():
    registrations = [{
        "id": "R1",
        "event_id": "E001",
        "status": "confirmed"
    }]

    checked = check_in_attendee(registrations, "R1")

    assert checked["checked_in"] is True
    assert "checked_in_at" in checked
    assert checked["status"] == "confirmed"
