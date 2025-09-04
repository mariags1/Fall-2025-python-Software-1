#ask the user how many random points to generate
import random
points = int(input("How many times you want to generate a point: "))
circle_points = 0
square_point = 0
counter = 0
#calculate the approximate value of pi
while counter < points:
    counter = counter + 1

    x = random.uniform(1, -1)
    y = random.uniform(-1, 1)

    value = x ** 2 + y ** 2 < 1

    if value == True:
        circle_points = circle_points + 1

print(4 * circle_points/points)

#prints out the approximation of pi