def add_vehicle(vehicles):
    print("\n--- Add Vehicle ---")

    number = input("Enter vehicle number: ")
    vehicle_type = input("Enter vehicle type: ")
    capacity = input("Enter vehicle capacity: ")

    vehicle = {
        "number": number,
        "type": vehicle_type,
        "capacity": capacity
    }

    vehicles.append(vehicle)

    print("Vehicle added successfully!")


def show_vehicles(vehicles):
    print("\n--- Vehicle List ---")

    if len(vehicles) == 0:
        print("No vehicles available.")
        return

    for vehicle in vehicles:
        print("Vehicle Number:", vehicle["number"])
        print("Vehicle Type:", vehicle["type"])
        print("Capacity:", vehicle["capacity"])
        print("--------------------")