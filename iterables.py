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

name = "Qamro Bakhouche" # this is a string, which is an iterable
for letter in name:
    print(letter, end=" ")
print()        

dict = {"name": "Qamro", "age": 18, "city": "Sétif"} # this is a dictionary, which is an iterable
for key, value in dict.items(): 
    print(f"{key}: {value}")  # return both key and value
print()
for key in dict.keys():
    print(key)  # return only keys
print()
for value in dict.values():
    print(value)  # return only values  
print()    