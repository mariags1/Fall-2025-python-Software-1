import random

number1 = random.randint(0,9)
number2 = random.randint(0,9)
number3 = random.randint(0,9)

code = str(number1) + str(number2) + str(number3)

print("3-digit code:",code)

num1 = random.randint(1,6)
num2 = random.randint(1,6)
num3 = random.randint(1,6)
num4 = random.randint(1,6)

code2 = str(num1)+str(num2)+str(num3)+str(num4)

print("4-digit code:", code2)