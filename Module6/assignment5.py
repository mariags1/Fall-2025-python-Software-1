def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

original_list = [1,2,3,4,5,6,7,8,9,10]

filtered_list = filter_even_numbers(original_list)

print(f"Original list: {original_list}")
print(f"Even numbers only: {filtered_list}")
