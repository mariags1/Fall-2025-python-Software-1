def gallons_to_liters(gallons):
    return gallons * 3.785

while True:
    gallons = float(input("Enter the amount of gasoline in gallons: "))

    if gallons < 0:
        print("Exiting the program.")
        break
liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is equal to {liters:.3f} liters.\n")
