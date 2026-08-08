# list comprehension is a concise way to create lists in Python
# the format is: list = [expression for item in iterable if condition]

# instead of using for loop like this:
doubles = []
for x in range(1, 11):
    doubles.append(x*2)
print(doubles)
print()
# you can use list comprehension like this:
doubles = [x*2 for x in range(1, 11)]
print(doubles)
print()

# you can also add a condition to filter the items
numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
positive_numbers = [num for num in numbers if num >= 0]
print(positive_numbers)
print()
negative_numbers = [num for num in numbers if num < 0]
print(negative_numbers)
print()
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
print()
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)
print()

# you can also use list comprehension to create a list of tuples
square_tuples = [(x, x**2) for x in range(1, 6)]
print(square_tuples)
print()