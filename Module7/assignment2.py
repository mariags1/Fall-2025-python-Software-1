names = set() # Use a set to store names

while True:
    name = input("Enter a name (or press Enter to finish): ")
    if name == "":
        break  # Stop if empty string is entered

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nList of entered names:")
for n in names:
    print(n)