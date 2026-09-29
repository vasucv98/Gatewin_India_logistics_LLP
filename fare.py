def calculate_fare():
    print("\n--- Fare Calculator ---")

    distance = float(input("Enter distance in km: "))
    rate = float(input("Enter rate per km: "))

    fare = distance * rate

    print("Distance:", distance, "km")
    print("Rate:", rate, "per km")
    print("Total Fare:", fare)