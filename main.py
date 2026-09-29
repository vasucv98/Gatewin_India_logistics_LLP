import booking
import vehicle
import driver
import fare


bookings = []
vehicles = []
drivers = []


while True:

    print("\n================================")
    print("GATEWIN INDIA LOGISTICS LLP")
    print("================================")

    print("1. Add Transport Booking")
    print("2. Show Bookings")
    print("3. Add Vehicle")
    print("4. Show Vehicles")
    print("5. Add Driver")
    print("6. Show Drivers")
    print("7. Calculate Fare")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        booking.book_transport(bookings)

    elif choice == "2":
        booking.show_bookings(bookings)

    elif choice == "3":
        vehicle.add_vehicle(vehicles)

    elif choice == "4":
        vehicle.show_vehicles(vehicles)

    elif choice == "5":
        driver.add_driver(drivers)

    elif choice == "6":
        driver.show_drivers(drivers)

    elif choice == "7":
        fare.calculate_fare()

    elif choice == "8":
        print("Thank you for using GATEWIN INDIA LOGISTICS LLP")
        break

    else:
        print("Invalid choice. Please try again.")