# Event Registration & Check-In Platform

## Project Overview
This project is a terminal-based Event Registration and Check-In Platform developed in Python.  
It is designed to help conference or event organizers manage events, attendee registrations, ticketing, and on-site check-in workflows in an offline environment.

The system supports event creation, attendee management, registration with capacity control, waitlist handling, check-in operations, reporting, and data persistence using JSON files.

---

## Features

### Event & Session Management
- Create and update events with details such as name, location, date, capacity, and price
- Manage sessions/workshops for events
- Persist event data using JSON files

### Attendee Management
- Register new attendees with profile information
- Authenticate attendees using email and PIN
- Update attendee information

### Registration & Ticketing
- Register attendees for events
- Enforce event capacity limits
- Automatically place attendees on a waitlist when events are full
- Promote waitlisted attendees when slots become available
- Generate confirmation codes for registrations

### Check-In & Badge Generation
- Check in confirmed attendees on event day
- Log check-in timestamps for analytics
- Generate text-based badges for attendees

### Reporting & Analytics
- Attendance reports (registered vs checked-in)
- Revenue reports per event
- Session popularity analysis
- Export reports to text files

### Persistence & Backup
- Save system state using JSON files
- Create timestamped backups
- Validate registration data integrity

### Testing
- Automated tests for:
  - Capacity enforcement
  - Waitlist promotion
  - Check-in logging
  - Attendance reporting

---

## Project Structure

```text
project/
├── main.py
├── events.py
├── attendees.py
├── registration.py
├── checkin.py
├── reports.py
├── storage.py
├── data/
│   ├── events.json
│   ├── attendees.json
│   └── registrations.json
├── tests/
│   ├── test_registration.py
│   ├── test_checkin.py
│   └── test_reports.py
└── README.md
```


---
## How to Run the Application

1. Ensure Python 3.9+ is installed
2. Navigate to the project directory
3. Run the main application:

```bash
python main.py
```



