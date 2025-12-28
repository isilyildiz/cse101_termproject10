
from attendees import (
    load_attendees,
    save_attendees,
    register_attendee,
    authenticate_attendee,
    update_attendee
)

from registration import (
    load_registrations,
    save_registrations,
    create_registration
)

from events import load_events, save_events, create_event


ATTENDEES_PATH = "data/attendees.json"
EVENTS_PATH = "data/events.json"
REG_PATH = "data/registrations.json"


#main menu

def main():
    print("\n=== EVENT REGISTRATION PLATFORM ===")
    print("1. Organizer Actions")
    print("2. Attendee Menu")
    print("3. Exit")

    choice = input("Select: ")

    if choice == "1":
        organizer_menu()

    if choice == "2":
        attendee_menu()

    if choice == "3":
        print("Goodbye!")
        return

    main()


#organizer menu
def organizer_menu():
    events = load_events(EVENTS_PATH)

    print("\n=== Organizer Menu ===")
    print("1. Add Event")
    print("2. Show Event Count")
    print("3. Update Event")
    print("4. Back")


    choice = input("Select: ")

    if choice == "1":
        new_event = {
            "id": input("Event ID: "),
            "name": input("Event Name: "),
            "location": input("Location: "),
            "start_date": input("Start Date: "),
            "end_date": input("End Date: "),
            "capacity": int(input("Capacity: ")),
            "price": float(input("Price: ")),
            "description": input("Description: "),
            "sessions": []
        }

        create_event(events, new_event)
        save_events(EVENTS_PATH, events)
        print("Event added successfully.")

    if choice == "2":
        print("Registered event count:", len(events))

    if choice == "3":
       event_id = input("Event ID to update: ")
       new_name = input("New Event Name (leave blank to skip): ")
       new_capacity = input("New Capacity (leave blank to skip): ")

       updates = {}

       if new_name:
           updates["name"] = new_name
       if new_capacity:
           updates["capacity"] = int(new_capacity)

       from events import update_event
       updated = update_event(events, event_id, updates)

       if updated:
           save_events(EVENTS_PATH, events)
           print("Event updated successfully.")
       else:
           print("Event not found.")

    if choice == "4":
       main()


    organizer_menu()


#attendee menu
def attendee_menu():
    attendees = load_attendees(ATTENDEES_PATH)
    registrations = load_registrations(REG_PATH)
    events = load_events(EVENTS_PATH)

    print("\n=== Attendee Menu ===")
    print("1. Register as a New Attendee")
    print("2. Login")
    print("3. Back")

    choice = input("Select: ")

    if choice == "1":
        name = input("Name: ")
        email = input("Email: ")
        pin = input("PIN (4 digits): ")

        profile = {"name": name, "email": email, "pin": pin}
        new_att = register_attendee(attendees, profile)

        save_attendees(ATTENDEES_PATH, attendees)
        print("\nAttendee registered. Your ID:", new_att["id"])

    if choice == "2":
        email = input("Email: ")
        pin = input("PIN: ")

        user = authenticate_attendee(attendees, email, pin)

        if user:
            print("\nLogin successful.")
            attendee_logged_in_menu(user)
        else:
            print("\nLogin failed.")

    if choice == "3":
        main()

    attendee_menu()


#attendee logged in menu

def attendee_logged_in_menu(user):
    attendees = load_attendees(ATTENDEES_PATH)
    registrations = load_registrations(REG_PATH)
    events = load_events(EVENTS_PATH)

    print(f"\n=== Welcome, {user['name']} ===")
    print("1. View My Info")
    print("2. Update My Info")
    print("3. Register to Event")
    print("4. Logout")

    choice = input("Select: ")

    if choice == "1":
        print("\nMy Information:")
        print(user)

    if choice == "2":
        new_name = input("New Name (leave blank to skip): ")
        new_org = input("New Organization (optional): ")

        updates = {}

        if new_name:
            updates["name"] = new_name

        if new_org:
            updates["organization"] = new_org

        update_attendee(attendees, user["id"], updates)
        save_attendees(ATTENDEES_PATH, attendees)
        print("\nInformation updated!")

    if choice == "3":
        print("\nAvailable Events:")
        for e in events:
            print(e["id"], "-", e["name"])

        event_id = input("Enter Event ID: ")

        reg_data = {
            "attendee_id": user["id"],
            "event_id": event_id
        }

        reg = create_registration(registrations, reg_data, events)
        save_registrations(REG_PATH, registrations)

        print("\nEvent registration completed!")
        print("Confirmation:", reg["confirmation_code"])

    if choice == "4":
        attendee_menu()

    attendee_logged_in_menu(user)


if __name__ == "__main__":
    main()
