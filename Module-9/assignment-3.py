"""""
Extend the previous exercise's Car class by adding a new drive method 
that receives the number of hours as a parameter. 
The method increases the travelled distance by how much the car has travelled in constant speed 
in the given time.

Example: The travelled distance of car object is 2000 km. 
The current speed is 60 km/h. 
Method call car.drive(1.5) increases the travelled distance to 2090 km.
"""""

class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, new_speed):
        self.current_speed += new_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
