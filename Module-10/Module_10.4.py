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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change_of_speed = random.randint(-10, 15)
            car.accelerate(change_of_speed)
            car.drive(1)

    def print_status(self):
        print(f"\n{'Plate':<10}{'MaxSpd':<10}{'CurSpd':<10}{'Distance':<10}")
        print("-" * 40)
        for car in self.cars:
            print(f"{car.license_plate:<10}"
                  f"{car.maximum_speed:<10}"
                  f"{car.current_speed:<10}"
                  f"{car.travelled_distance:<10.1f}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
race = Race("Grand Python Prix", 10000, cars)

while not race.race_finished():
    race.hour_passes()

race.print_status()
print("\nRace finished!")
