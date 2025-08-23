#Requirements:
#The program should prompt the user with "Enter the radius of the circle: "
#The program should calculate the area
#The program should output the area in the form "The area of the circle is [area]"
#Store the radius in a variable called 'radius'
#Store the area in a variable called 'area'

import math
user = input("Enter the radius of the circle: ")
radius = float(user)

# Formula A = πr2
area = (math.pi*(radius ** 2))

print("The area of the circle is ", area)


