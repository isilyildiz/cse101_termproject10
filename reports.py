def attendance_report(events: list, registrations: list) -> dict:
    report = {}

    for e in events:
        event_id = e["id"]
        registered = 0
        checked_in = 0

        for r in registrations:
            if r["event_id"] == event_id:
                registered += 1
                if r.get("checked_in"):
                    checked_in += 1

        report[event_id] = {
            "registered": registered,
            "checked_in": checked_in
        }

    return report


def revenue_report(events: list, registrations: list) -> dict:
    report = {}

    for e in events:
        total = 0.0
        for r in registrations:
            if (
                r["event_id"] == e["id"]
                and r["status"] == "confirmed"
                and r["payment_status"] == "paid"
            ):
                total += e["price"]

        report[e["id"]] = total

    return report


def session_popularity(events: list, registrations: list) -> dict:
    popularity = {}

    for r in registrations:
        event_id = r["event_id"]
        popularity[event_id] = popularity.get(event_id, 0) + 1

    return popularity


def export_report(report: dict, filename: str) -> str:
    with open(filename, "w", encoding="utf-8") as f:
        for key, value in report.items():
            f.write(f"{key}: {value}\n")

    return filename
