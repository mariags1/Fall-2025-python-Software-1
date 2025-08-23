#Requirements:
#The program should prompt the user with "Enter the length of the rectangle: "
#The program should prompt the user with "Enter the width of the rectangle: "
#The program should calculate the perimeter and area
#The program should output the perimeter in the form "The perimeter of the rectangle is [perimeter]"
#The program should output the area in the form "The area of the rectangle is [area]"
#Store the length in a variable called 'length'
#Store the width in a variable called 'width'
#Store the perimeter in a variable called 'perimeter'
#Store the area in a variable called 'area'

import math
user = input("Enter the length of the rectangle: ")
user2 = input("Enter the width of the rectangle: ")

# Perimeter u = 2(a+b), Area A = ab
length = float(user)
width = float(user2)

perimeter = 2* (length+width)
area = length*width

print("The perimeter of the rectangle is", perimeter)
print("The area of the rectangle is", area)
