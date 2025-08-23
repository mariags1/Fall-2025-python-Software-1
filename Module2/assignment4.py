#Requirements:
#The program should prompt the user with "Enter the first integer: "
#The program should prompt the user with "Enter the second integer: "
#The program should prompt the user with "Enter the third integer: "
#The program should calculate the sum, product, and average of the numbers
#The program should output the sum in the form "The sum of the numbers: [sum]"
#The program should output the product in the form "The product of the numbers: [product]"
#The program should output the average in the form "The average of the numbers: [average]"
#Store the first number in a variable called 'num1'
#Store the second number in a variable called 'num2'
#Store the third number in a variable called 'num3'
#Store the sum in a variable called 'sum_of_numbers'
#Store the product in a variable called 'product_of_numbers'
#Store the average in a variable called 'average_of_numbers'

first = input("Enter the first integer: ")
second = input("Enter the second integer: ")
third = input("Enter the third integer: ")

num1 = int(first)
num2 = int(second)
num3 = int(third)

sum_of_numbers = num1 + num2 + num3
product_of_numbers = num1 * num2 * num3
average_of_numbers = sum_of_numbers/3

print("The sum of the numbers:", sum_of_numbers)
print("The product of the numbers:", product_of_numbers)
print("The average of the numbers:", average_of_numbers)
