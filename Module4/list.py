#making lists

names = ["Anna", "Maria", "Sophie", "Matti"]
print(names[-1]) #gives the last name
print(names[0]) #gives the first name

print(names[0:3]) #gives first three names
print(names[3:])

names[1] = "Susan" #changes name "Maria" to "Susan"
print(names)

names.append("Susan") #Adds Susan
print(names)

names.insert(1,"Aslan") #inserts Aslan by removing Maria
print(names)

names.pop(1)
print(names)

for name in names:
    print(name) #prints names one by one

for i in range(1,10):
    print(i) #print range of numbers
    print(names[i]) #print a number for each name