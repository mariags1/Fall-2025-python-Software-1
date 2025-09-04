# Write a program that asks the user for a username and password.
username = input("Enter username: ")
password = input("Enter password: ")
tries = 1
# If either or both are incorrect, the program asks the user to enter the username and password again.
while username != "python" or password != "rules":
    print("Incorrect username or password. Please try again.")

# This continues until the login information is correct or wrong credentials have been entered five times.
# After five failed attempts the program prints out "Access denied".
    if tries < 5:
        username = input("Enter username: ")
        password = input("Enter password: ")

    tries = tries+1
    if tries == 5:
        print("Access denied.")
        break
# If the information is correct, the program prints out "Welcome".
else:
    print("Welcome!")
# The correct username is python and password rules.



