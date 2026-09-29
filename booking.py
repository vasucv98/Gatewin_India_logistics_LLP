def book_transport(bookings):
    print("\n--- Transport Booking ---")

    name = input("Enter customer name: ")
    pickup = input("Enter pickup place: ")
    destination = input("Enter destination: ")
    vehicle = input("Enter vehicle type: ")

    booking = {
        "name": name,
        "pickup": pickup,
        "destination": destination,
        "vehicle": vehicle
    }

    bookings.append(booking)

    print("Booking added successfully!")


def show_bookings(bookings):
    print("\n--- All Bookings ---")

    if len(bookings) == 0:
        print("No bookings found.")
        return

    for booking in bookings:
        print("Customer:", booking["name"])
        print("Pickup:", booking["pickup"])
        print("Destination:", booking["destination"])
        print("Vehicle:", booking["vehicle"])
        print("--------------------")