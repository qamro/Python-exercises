# membership operators in python are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).
# the 'in' operator returns True if the value is found in the sequence, otherwise it returns False.
# the 'not in' operator returns True if the value is not found in the sequence, otherwise it returns False.

fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # True
print("grape" in fruits)  # False
print("grape" not in fruits)  # True
print("banana" not in fruits)  # False
print()
print()

print("Exercise:")
secret_word = "python"
guess = input("Enter a letter in the secret word: ").lower()
if guess in secret_word:
    print("Good guess!")
else:
    print("Sorry, that letter is not in the secret word.")
print()
print()

print("Exercise 2:")
email = input("Enter your email address: ")
if "@" in email and "." in email:
    print("Valid email address.")
else:
    print("Invalid email address.")