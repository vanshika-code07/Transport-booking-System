import sqlite3

# Connect to the database
connection = sqlite3.connect("transport.db")

# Create cursor
cursor = connection.cursor()

# Create Vehicles table
cursor.execute("""create table if not exists Vehicles 
    (vehicle_id integer primary key autoincrement,
    vehicle_number text not null unique,
    vehicle_type text not null,
    capacity integer not null)""")

# Create Routes table
cursor.execute("""
create table if not exists Routes (
    route_id integer primary key autoincrement,
    source text not null,
    destination text not null,
    distance real not null
)
""")

# Create Schedules table
cursor.execute("""
create table if not exists Schedules (
    schedule_id integer primary key autoincrement,
    vehicle_id integer not null,
    route_id integer not null,
    travel_date text not null,
    departure_time text not null,
    arrival_time text not null,
    FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id),
    FOREIGN KEY (route_id) REFERENCES Routes(route_id)
)
""")

# Create Bookings table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Bookings (
    booking_id integer primary key autoincrement,
    schedule_id INTEGER NOT NULL,
    passenger_name TEXT NOT NULL,
    seats INTEGER NOT NULL,
    FOREIGN KEY (schedule_id) REFERENCES Schedules(schedule_id)
)
""")

# Save changes
connection.commit()

# Close database
connection.close()

print("Database and tables created successfully!")
