from reports import attendance_report

def test_attendance_report_counts():
    events = [{"id": "E001"}]

    registrations = [
        {"event_id": "E001", "checked_in": True},
        {"event_id": "E001", "checked_in": False}
    ]

    report = attendance_report(events, registrations)

    assert report["E001"]["registered"] == 2
    assert report["E001"]["checked_in"] == 1
