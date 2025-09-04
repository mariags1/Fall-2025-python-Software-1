# Write a program that asks the user to enter numbers until they enter an empty string to quit.
number = input("Enter a number (or press Enter to quit): ")
min_number = float(number)
max_number = float(number)

while True :

    if len(number) == 0:
        break
    else:
        if float(number) < min_number:
            min_number = float(number)
        elif float(number) > max_number:
            max_number = float(number)
        number = input("Enter a number (or press Enter to quit): ")

# Finally, the program prints out the smallest and largest number from the numbers it received.
print(f"Smallest number: {min_number}\nLargest number: {max_number}")

