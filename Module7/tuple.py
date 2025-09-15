days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
day_number = int(input("Enter the day number (1-7): "))
day = days_of_the_week[day_number - 1] # <---- index starts at 0 that is why -1
print(f"Day number {day_number} is {day}.")

#tuple UNPACKING
fruits = "Orange", "Banana", "Apple"
(first, second, third) = fruits # <----- can be unpacked into variable
print(f"The fruits are: {first}, {second} and {third}.")

#tuple AS RETURN VALUES
import random

def cast():
    first, second = random.randint(1,6), random.randint(1,6)
    return first, second

die1, die2 = cast() # <---- die1 = first , die2 = second
print(f"The dice show {die1} and {die2}.")