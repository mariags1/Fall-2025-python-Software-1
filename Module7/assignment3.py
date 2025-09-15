  # Dictionary to store ICAO code -> Airport name
airports = {}

while True:
    print("\nAirport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Please choose an option (1-3): ")

    if choice == "1":
        icao = input("Enter the ICAO code: ").upper()
        name = input("Enter the airport name: ")
        airports[icao] = name
        print(f"Airport {name} with ICAO code {icao} has been added.")

    elif choice == "2":
        icao = input("Enter the ICAO code: ").upper()
        if icao in airports:
            print(f"The airport with ICAO code {icao} is {airports[icao]}.")
        else:
            print("No airport found with ICAO code EFHK.")

    elif choice == "3":
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")