# iterables is an object or collection that can be iterated over, meaning you can loop through its elements one at a time.
# In Python, common examples of iterables include lists, tuples, strings, dictionaries, and sets.

numbers = [1, 2, 3, 4, 5] # this is a list, which is an iterable
for number in numbers:
    print(number)
print()
for number in reversed(numbers): 
    print(number)    
print()

numbers = (1, 2, 3, 4, 5) # this is a tuple, which is also an iterable
for number in numbers:
    print(number)
print()

fruits = {"apple", "banana", "cherry"} # this is a set, which is an iterable
for fruit in fruits:
    print(fruit)     
print()    

