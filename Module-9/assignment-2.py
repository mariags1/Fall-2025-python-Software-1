"""""
Extend the previous exercise's Car class by adding an accelerate method to it. 
The method receives the change of speed (km/h) as a parameter. 
If the change is negative, the car reduces speed. 
The method must change the value of the object's current_speed property. 
The speed of the car must stay below the set maximum and cannot be less than zero.
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






