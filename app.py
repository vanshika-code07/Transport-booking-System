from main import (
    add_vehicle,
    add_route,
    add_schedule,
    add_booking,
    view_vehicles,
    view_routes,
    view_schedules,
    view_bookings,
    search_vehicle,
    export_bookings)

def main():
    while True:
        print("\n")
        print(" TRANSPORT SCHEDULING SYSTEM")
        print("1. Add Vehicle")
        print("2. Add Route")
        print("3. Add Schedule")
        print("4. Add Booking")
        print("5. View Vehicles")
        print("6. View Routes")
        print("7. View Schedules")
        print("8. View Bookings")
        print("9. Search Vehicle")
        print("10. Export Booking Report")
        print("11. Exit")

        choice = input("\nEnter your choice: ")

        # ADD VEHICLE
        if choice == "1":
            vehicle_number = input("Enter vehicle number: ").strip()
            vehicle_type = input("Enter vehicle type: ").strip()
            try:
                capacity = int(input("Enter capacity: "))
                if capacity <= 0:
                    print("Capacity must be greater than 0.")
                    continue
                add_vehicle(vehicle_number, vehicle_type, capacity)
            except ValueError:
                print("Please enter a valid number.")

        # ADD ROUTE
        elif choice == "2":
            source = input("Enter source: ").strip()
            destination = input("Enter destination: ").strip()
            try:
                travel_distance = float(input("Enter distance in km: "))
                if travel_distance <= 0:
                    print("Please provide a distance longer than 0.")
                    continue
                add_route(source, destination, travel_distance)
            except ValueError:
                print("Please provide a valid distance.")

        # ADD SCHEDULE
        elif choice == "3":
            try:
                view_vehicles()
                vehicle_id = int(input("\nEnter vehicle ID: "))
                view_routes()
                route_id = int(input("\nEnter route ID: "))
                travel_date = input("Enter travel date (YYYY-MM-DD): ")
                departure_time = input("Enter departure time (HH:MM): ")
                arrival_time = input("Enter arrival time (HH:MM): ")
                add_schedule(vehicle_id, route_id, travel_date, departure_time, arrival_time)
            except ValueError:
                print("Please enter valid numbers.")

        # ADD BOOKING
        elif choice == "4":
            try:
                view_schedules()
                schedule_id = int(input("\nEnter schedule ID: "))
                passenger_name = input("Enter passenger name: ").strip()
                seats = int(input("Enter number of seats: "))
                add_booking(schedule_id, passenger_name, seats)
            except ValueError:
                print("Please enter valid numbers.")

        # VIEW VEHICLES
        elif choice == "5":
            view_vehicles()

        # VIEW ROUTES
        elif choice == "6":
            view_routes()

        # VIEW SCHEDULES
        elif choice == "7":
            view_schedules()

        # VIEW BOOKINGS
        elif choice == "8":
            view_bookings()

        # SEARCH VEHICLE
        elif choice == "9":
            vehicle_number = input("Enter vehicle number to search: ").strip()
            search_vehicle(vehicle_number)

        # EXPORT REPORT
        elif choice == "10":
            export_bookings()

        # EXIT
        elif choice == "11":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
