import random
# to generate random integer in a range
number = random.randint(1, 10)
print(number)
# to generate random float in a range
float = random.uniform(1, 10)
print(float)
# to generate a random float number between 0 and 1
x = random.random()
print(x)
# to choose a random element from a list, set, tuple, dictionary...etc
tuple_example = ("cristiano ronaldo", "magnus carlsen", "courtois")
option = random.choice(tuple_example)
print(option)
# to resort and rearrange randomly and shuffle a list, tuple, dictionary...etc
list_example = ["1", "2", "3", "A", "B", "C"]
random.shuffle(list_example)
print(list_example)
# to choose a specified number of random elements (like 3 random elements) from a list, set, tuple, dictionary...etc
fruits = ["apple", "strawberry", "banana", "orange", "kiwi", "cherry", "melon"]
random_fruits = random.sample(fruits, 2) # here we want to pick 2 random elements from fruits list
print(random_fruits)
random_fruits2 = random.sample(fruits, 3) # here we want to pick 3 random elements from fruits list
print(random_fruits2)
random_fruits3 = random.sample(fruits, 4) # here we want to pick 4 random elements from fruits list
print(random_fruits3)
