# 🚍 Transport Scheduling & Booking System

A Python + SQLite project to manage vehicles, routes, schedules and bookings. This project was implemented as a menu driven terminal based application that does not require any external dependencies.
## 🏗️ Implementation Details

This project was built using
- Python 3 (Core language + Menu based interface)

- SQLite (Embedded database)
- File logging (For audit logs)

- Report generation (To display booking reports)
The application comprises of various functions that are used to implement the desired features.
Functions such as
- `add_vehicle`, `add_route`, `add_schedule`, `add_booking` are used to add records to the database.
- `view_vehicles`, `view_routes`, `view_schedules`, `view_bookings` are used to display database records in a tabular format.
- `search_vehicle` is used to search for a vehicle using its number.
- `export_bookings` function is used to generate a report file containing all bookings.
A main loop is used to present a menu to the user and handle user input/output.
## ⚙️ Working
1. Database Connection
- The application connects to an embedded SQLite database (transport.db).
- The database contains 4 tables namely, `Vehicles`, `Routes`, `Schedules` and `Bookings`
2. Adding new records
- New `Vehicles` can be added by providing their number, type and capacity.
- New `Routes` can be added by providing source, destination and distance.
- New `Schedules` can be added by associating a vehicle and route to a particular date/time.
- `Bookings` can be made by reserving a certain number of seats in a vehicle for a particular route.

3. Viewing records
- The view functions display all the records in the respective database tables in a tabular format.
4. Searching for a vehicle
- The `search_vehicle` function allows searching for a vehicle using its registration number.
5. Exporting booking reports
- This is done using the `export_bookings` function. The records are exported to a file named `bookings_report.txt`
6. Logging
- All operations are logged in a file named `transport_log.txt`
## ✨ Features
| Feature | Description |
| --- | --- |
| ➕ | Add new records (Vehicles, Routes, Schedules, Bookings) |
| 🛣️ | View all Routes |
| 📅 | View all Schedules |
| 🎟️ | View all Bookings |
| 🔍 | Search for a vehicle by its number |
| 📄 | Export booking reports to a file |
| 📝 | Log of all operations performed |
## 🛠️ Requirements
- Python 3
- SQLite (Built into Python)
## ▶️ Usage

1. Clone the repository
```bash
git clone https://github.com/vanshika-code07/transport-booking-system.git
```