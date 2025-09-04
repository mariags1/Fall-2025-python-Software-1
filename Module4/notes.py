#while loop

counter = 0
while counter < 20:
    print("Maria")
    counter = counter + 1 #loops back to while, repeats until 19 (my name will be printed 20 times)

print("We are now out of the while loop") #will only be printed once

rounds = int(input("How many greeting: ")) #needs int() to create string
i = 0
while i < rounds:
    print("Hello")
    i = i + 1 #without this you are stuck in an infinite loop

print("We are now out of the while loop")