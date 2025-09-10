#asks the user for an integer
integer = int(input("Enter an integer: "))

#The program should tell if the number is a prime number or no
if integer <= 1:
    print(f"{integer} is not a prime number.")

else:
    for i in range (2, integer):
        if integer % i == 0: # % = 0 (has no remainder) it is not a prime number
            print(f"{integer} is not a prime number.")
            break

    else:
        print(f"{integer} is a prime number.")

