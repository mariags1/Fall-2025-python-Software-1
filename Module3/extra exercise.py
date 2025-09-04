customer = input("Enter the customer(Elves, Wizards, Ghosts): ").lower()
age = int(input("Customers age: "))

if customer == "elves":
    if age>=100:
        print("You can buy sparkling water and Leaf Drinks")
    elif age<100:
        print("you can buy sparkling water")

if customer == "wizards":
    if age>=21:
        print("you can buy sparkling water and wine")
    elif age<21:
        print("you can buy sparkling water")

if customer == "ghosts":
    print("you can buy sparkling water and dust cookies")

