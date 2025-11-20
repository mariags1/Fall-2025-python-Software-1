class Dog: #defines a class named Dog
    pass


dog = Dog() #statement that creates a Dog object
dog.name = "Bubbles" # property of the object
dog.birth_year = 2022 #  property of the object

print(f"{dog.name:s} was born in {dog.birth_year:d}.")
#The first statement in the main program creates a Dog object that is referenced by the variable dog.

"""""
If we want more dog we need to create more objects:

dog1 = Dog()
dog1.name = "Bubbles"
dog1.birth_year = 2022

dog2 = Dog()
dog2.name = "Rex"
dog2.birth_year = 2020

dog3 = Dog()
dog3.name = "Luna"
dog3.birth_year = 2023
"""""