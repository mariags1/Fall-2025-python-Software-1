from operator import truediv

string = "string, any text will do"
string2 = "hello"

print(string + string2) #printing the content of the string and strings
# + or , can be used to add both variables

# "" will print the actual word (without "" it will print the variable)

numbers = 1234 #numbers is the name we choose for the variable
number = 1

print(numbers + number)
#cannot print(number + string) because

boolean = True #needs to be capital
boolean2 = False

k = "Matti" #with k we do not know what the variable is so it is better to say Name instead of k

amount_of_money = 100
person_name = "Matti"

print(person_name + " has money: " + str(amount_of_money)) #str() is to help python work with text and numbers

#input funtion will always give a string
value = input("Give number: ")
print(value)

print("The given value + 50 = " + value +str(50))
print("The given value + 50 = " + str(int(value) + 50)) #int()
