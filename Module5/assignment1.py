# Write a program that asks the user how many dice to roll.

import random
num = int(input("How many roll: "))
total = 0

for i in range(num):
    roll = random.randint(1,6)
    total += roll

# The program rolls all the dice once and prints out the sum of the numbers.
# Use a for loop.

print(f"The total sum of all {num} dice is: {total}")