#write a program that asks a fisher the length of a zander
zander = float(input("Enter the length of the zander in centimeters: "))


if zander<42:
    print("The zander does not meet the size limit.\nPlease release the fish back into the lake.")
    missing_cm = 42-zander
    print(f"The fish was {missing_cm:.1f} centimeters below the size limit.")

if zander>=42:
    print("The zander meets the size limit.")

# \n is used to made a second line.
# .1f: a float with the accuracy of 1 decimal