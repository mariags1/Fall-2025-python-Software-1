#ask the user to enter numbers until they input an empty string
numbers = []

while True:
    num = input("Enter numbers: ")
    if num == "":
       break
    numbers.append(int(num))

#prints out the five greatest numbers sorted in descending order

numbers.sort(reverse=True)

print("The five greatest numbers in descending order:")
for i in range(min(5, len(numbers))):
    print(numbers[i])

