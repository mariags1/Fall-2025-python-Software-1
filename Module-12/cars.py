import random
cars = []
for x in range(1, 11):
    license_plate = f"ABC-{x}"
    maximum_speed = random.randint(100, 200)
    #car = Car(license_plate, maximum_speed)
    #cars.append(car)
    cars.append(license_plate)
print(cars)