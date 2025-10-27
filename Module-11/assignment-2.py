"""""
Extend the previously written Car class by adding two subclasses: 
ElectricCar and GasolineCar. 
Electric cars have the capacity of the battery in kilowatt-hours as their property (battery_capacity). 
Gasoline cars have the volume of the tank in liters as their property (tank_volume). 
Write initializers for the subclasses. 
For example, the initializer of electric cars receives the registration number (license_plate), 
maximum speed (maximum_speed) and battery capacity (battery_capacity) as its parameter. 
It calls the initializer of the base class to set the first two properties and then sets its capacity.

Requirements:

Write the complete Car base class with initializer and methods
Create ElectricCar subclass with battery_capacity property
Create GasolineCar subclass with tank_volume property
"""""

import random

class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        new_speed = self.current_speed + change_of_speed
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


def race():
    cars = []
    for i in range(1, 11):
        license_plate = f"ABC-{i}"
        maximum_speed = random.randint(100, 200)
        car = Car(license_plate, maximum_speed)
        cars.append(car)
    race_over = False
    while not race_over:
        for car in cars:
            change_of_speed = random.randint(-10, 15)
            car.accelerate(change_of_speed)
            car.drive(1)
            if car.travelled_distance >= 10000:
                race_over = True

    return sorted(cars, key=lambda c: c.travelled_distance, reverse=True)

class Race:
    def __init__ (self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

def hour_passes(self):
    for car in self.cars:
        change_of_speed = random.randint(-10, 15)
        car.accelerate(change_of_speed)
        car.drive(1)
def print_status(self):
    print(f"{'License Plate':<15}{'Max Speed':<12}{'Current Speed':<15}{'Distance':<10}")
    print("-" * 55)
    for car in self.cars:
        print(
             f"{car.license_plate:<15}{car.maximum_speed:<12}{car.current_speed:<15}{car.travelled_distance:<10.1f}")

def race_finished(self):
    for car in self.cars:
        if car.travelled_distance >= self.distance:
             return True
    return False

class ElectricCar(Car):
    def __init__(self, license_plate, maximum_speed, battery_capacity):
        super().__init__(license_plate, maximum_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, license_plate, maximum_speed, tank_volume):
        super().__init__(license_plate, maximum_speed)
        self.tank_volume = tank_volume