import sqlite3
# =i= DATABASE CONNECTION

def connect_db():
    return sqlite3.connect('transport.db')

def save_log(message):
    with open('transport_log.txt', 'a') as file:
        file.write(message + '\n')

def add_vehicle(vehicle_number, vehicle_type, cap):
    connection = connect_db()
    cursor = connection.cursor()
    try:
        cursor.execute('''
        INSERT INTO Vehicles (vehicle_number, vehicle_type, capacity)
        VALUES (?, ?, ?)
        ''', (vehicle_number, vehicle_type, cap))
        connection.commit()
        print('\nVehicle added successfully.')
        save_log('Vehicle added: ' + vehicle_number)
    except sqlite3.IntegrityError:
        print('\nVehicle already exists.')
    finally:
        connection.close()

def add_route(source, destination, distance):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO Routes (source, destination, distance)
    VALUES (?, ?, ?)
    ''', (source, destination, distance))
    connection.commit()
    connection.close()
    print('\nRoute added successfully.')
    save_log('Route added: ' + source + ' -> ' + destination)


def add_schedule(vehicle_id, route_id, travel_date, departure_time, arrival_time):
    connection = connect_db()
    cursor = connection.cursor()

    # Check vehicle
    cursor.execute('SELECT * FROM Vehicles WHERE vehicle_id = ?', (vehicle_id,))
    vehicle = cursor.fetchone()
    if not vehicle:
        print("Vehicle doesn't exist.")
        connection.close()
        return

    # Check route
    cursor.execute('SELECT * FROM Routes WHERE route_id = ?', (route_id,))
    route = cursor.fetchone()
    if not route:
        print("Route doesn't exist.")
        connection.close()
        return

    cursor.execute('''
    INSERT INTO Schedules (vehicle_id, route_id, travel_date, departure_time, arrival_time)
    VALUES (?, ?, ?, ?, ?)
    ''', (vehicle_id, route_id, travel_date, departure_time, arrival_time))
    connection.commit()
    connection.close()
    print('\nSchedule added successfully.')
    save_log('Schedule added for date: ' + str(travel_date))


def add_booking(schedule_id, name, requested_seats):
    connection = connect_db()
    cursor = connection.cursor()

    # Find capacity of vehicle
    cursor.execute('''
    SELECT Vehicles.capacity
    FROM Schedules
    JOIN Vehicles ON Schedules.vehicle_id = Vehicles.vehicle_id
    WHERE Schedules.schedule_id = ?
    ''', (schedule_id,))
    capacity = cursor.fetchone()
    if not capacity:
        print('Schedule does not exist.')
        connection.close()
        return

    # Find already booked seats
    cursor.execute('SELECT SUM(seats) FROM Bookings WHERE schedule_id = ?', (schedule_id,))
    booked = cursor.fetchone()[0] or 0
    available = capacity[0] - booked

    print('\nCapacity:', capacity[0])
    print('Already booked:', booked)
    print('Available seats:', available)

    if requested_seats <= 0:
        print('Please select a positive number of seats.')
        connection.close()
        return

    if requested_seats > available:
        print('Not enough available seats.')
        connection.close()
        return

    cursor.execute('''
    INSERT INTO Bookings (schedule_id, passenger_name, seats)
    VALUES (?, ?, ?)
    ''', (schedule_id, name, requested_seats))
    connection.commit()
    connection.close()
    print('\nBooking successful.')
    save_log('Booking for ' + name + ' of ' + str(requested_seats) + ' seats')

def view_vehicles():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Vehicles')
    vehicles = cursor.fetchall()
    print('\n========== VEHICLES ==========')
    for vehicle in vehicles:
        print('ID:', vehicle[0], '| Number:', vehicle[1], '| Type:', vehicle[2], '| Capacity:', vehicle[3])
    connection.close()

def view_routes():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Routes')
    routes = cursor.fetchall()
    print('\n========== ROUTES ==========')
    for route in routes:
        print('ID:', route[0], '|', route[1], '->', route[2], '| Distance:', route[3], 'km')
    connection.close()

def view_schedules():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''
    SELECT Schedules.schedule_id, Vehicles.vehicle_number, Routes.source, Routes.destination,
           Schedules.travel_date, Schedules.departure_time, Schedules.arrival_time
    FROM Schedules
    JOIN Vehicles ON Schedules.vehicle_id = Vehicles.vehicle_id
    JOIN Routes ON Schedules.route_id = Routes.route_id
    ''')
    schedules = cursor.fetchall()
    print('\n========== SCHEDULES ==========')
    for schedule in schedules:
        print('ID:', schedule[0], '| Vehicle:', schedule[1], '| Route:', schedule[2], '->', schedule[3],
              '| Date:', schedule[4], '||', schedule[5], '-', schedule[6])
    connection.close()


def view_bookings():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''
    SELECT Bookings.booking_id, Bookings.passenger_name, Bookings.seats, Schedules.schedule_id
    FROM Bookings
    JOIN Schedules ON Bookings.schedule_id = Schedules.schedule_id
    ''')
    bookings = cursor.fetchall()
    print('\n========== BOOKINGS ==========')
    for booking in bookings:
        print('Booking ID:', booking[0], '| Passenger:', booking[1], '| Seats:', booking[2], '| Schedule ID:', booking[3])
    connection.close()

def search_vehicle(vehicle_number):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Vehicles WHERE vehicle_number = ?', (vehicle_number,))
    vehicle = cursor.fetchone()
    if vehicle:
        print('\nVehicle found.')
        print('ID:', vehicle[0], 'Number:', vehicle[1], 'Type:', vehicle[2], 'Capacity:', vehicle[3])
    else:
        print('\nVehicle not found.')
    connection.close()


def export_bookings():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT booking_id, passenger_name, seats, schedule_id FROM Bookings')
    bookings = cursor.fetchall()
    connection.close()

    with open('bookings_report.txt', 'w') as file:
        file.write('TRANSPORT BOOKING REPORT\n')
        file.write('=======================\n')
        for booking in bookings:
            file.write(f'\nBooking ID: {booking[0]}\n')
            file.write(f'Passenger: {booking[1]}\n')
            file.write(f'Seats: {booking[2]}\n')
            file.write(f'Schedule ID: {booking[3]}\n')
            file.write('--------------------------\n')

    print('\nBooking report created successfully.')
