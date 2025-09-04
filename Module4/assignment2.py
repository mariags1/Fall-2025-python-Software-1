inches = float(input("Enter length in inches (negative value to quit: )"))

while inches >= 0:
    inches_in_cm = inches * 2.54
    print(f"{inches} inches is {inches_in_cm:.2f} centimeters.")

    inches = float(input("Enter length in inches (negative value to quit: )"))

print("Program ended.")

# print(f"{inches} inches is {inches_in_cm:.2f} centimeters")
# :.2f creates the decimal