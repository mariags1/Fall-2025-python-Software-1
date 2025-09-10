import random

#the number of sides on the dice as a parameter
def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input("Enter the number of sides on the dice: "))

max_number = sides
roll = 0
attempts = 0

while roll != max_number:
        roll = roll_dice(sides)
        attempts += 1
        print(roll)