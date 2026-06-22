name = input("Enter your full name: ")

print(f"Hello, {name}!")

# string manipulation


# count the number of words in the string (The split() method splits the string into a list of words based on whitespace by default.)
word_count = len(name.split())
print(f"Number of words in name: {word_count}")

#capitalize the first letter of your string
capitalized_name = name.capitalize()
print(f"Capitalized name: {capitalized_name}")
# convert the string to uppercase
uppercase_name = name.upper()
print(f"Uppercase name: {uppercase_name}")
# convert the string to lowercase
lowercase_name = name.lower()
print(f"Lowercase name: {lowercase_name}")
# count the number of characters in the string or the length of the string  
name_length = len(name)   
print(f"Length of name: {name_length}") 
# count the number of times a character appears in the string       
word_count = name.count('k')
print(f"Number of times 'k' appears in name: {word_count}")
# reverse the string (this syntax [::-1] is called slicing and it is used to reverse string or list or set or tuple and the -1 it is the step of the reversing and we can skip some characters by changing the step to -2 or -3 or -4 etc)   
reversed_name = name[::-1]
print(f"Reversed name: {reversed_name}")    
# find a character in the string 
character = input("Enter a character to find: ")
if character in name:
    print(f"Character '{character}' found in name.")
else:
    print(f"Character '{character}' not found in name.")
    
# find the index of a character in the string  (generally the index of a character is the position of the character in the string and it starts from 0 and it is used to find the position of a character in a string and when we get -1 it means the character is not found in the string) 
character = input("Enter a character to find its index: ")
index = name.find(character)
if index != -1:
    print(f"Character '{character}' found at index {index}.")
else:   
    print(f"Character '{character}' not found in name.")

# replace a character in the string
old_character = input("Enter the character to replace: ")
new_character = input("Enter the new character: ")
replaced_name = name.replace(old_character, new_character)
print(f"Replaced name: {replaced_name}")

# check if the string contains only alphabets
if name.isalpha():
    print("Name contains only alphabets.")
else:
    print("Name contains characters other than alphabets.") 
    
# check if the string contains only digits
if name.isdigit():
    print("Name contains only digits.")
else:
    print("Name contains characters other than digits.")               



# and finally here are all string methods that can be used to manipulate strings in python
print(help(str))    
    
        