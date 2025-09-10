# asks the user to enter the names of five cities one by one
cities = []

# stores them into a list structure
for city in range(5):
    city = input("Enter the name of city: ")
    cities.append(city)


print(f"The cities you entered: ")
for city in cities:
    print(city)

