def add_driver(drivers):
    print("\n--- Add Driver ---")

    name = input("Enter driver name: ")
    license_no = input("Enter driving license number: ")
    phone = input("Enter phone number: ")

    driver = {
        "name": name,
        "license": license_no,
        "phone": phone
    }

    drivers.append(driver)

    print("Driver added successfully!")


def show_drivers(drivers):
    print("\n--- Driver List ---")

    if len(drivers) == 0:
        print("No drivers found.")
        return

    for driver in drivers:
        print("Driver Name:", driver["name"])
        print("License Number:", driver["license"])
        print("Phone:", driver["phone"])
        print("--------------------")