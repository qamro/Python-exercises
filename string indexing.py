#string indexing is the process of accessing individual characters in a string using their index. 
#In Python, string indexing starts at 0, which means that the first character of a string is at index 0, the second character is at index 1, and so on. 
#You can use square brackets [] to access characters in a string by their index.
#[start:stop:step] is the syntax of slicing and it is used to access a range of characters in a string 
#the start is the index of the first character to be accessed
#the stop is the index of the last character to be accessed 
# the end index in both the arrays and the strings is exclusive 
# the last index in our array for example is 4 when we use him as an end index and it is 3 when we use him as a start index
# this case is only for the end index
#the step is the number of characters to skip between each character accessed (default is 1).
name = input("Enter your name: ")   
print(f"First character: {name[0]}")
print(f"Last character: {name[-1]}")
print(f"Characters from index 1 to 5: {name[1:5]}")
print(f"Characters from index 0 to the end: {name[0:]}")
print(f"Characters from the beginning to index 4: {name[:4]}")
print(f"Characters from index 0 to the end with a step of 2: {name[0::2]}") 
print(f"Characters from index 1 to the end with a step of 3: {name[1::3]}") 
print(f"Characters from the beginning to index 5 with a step of 2: {name[:5:2]}")   
print(f"Characters from index 0 to the end (the whole string) with a step of 3: {name[::3]}")
print(f"Characters from index 1 to index 10 with a step of 2: {name[1:10:2]}")  
print(f"Characters from index 0 to index 5 with a step of 1: {name[0:5:1]}")
print(f"Characters from index 0 to index 5 with a step of 2: {name[0:5:2]}")
print(f"Characters from index 0 to index 5 with a step of 3: {name[0:5:3]}")
print(f"all characters in reverse order: {name[::-1]}")
print(f"Characters from index 0 to index 5 in reverse order: {name[0:5:-1]}")
print(f"Characters from index 5 to index 0 in reverse order: {name[5:0:-1]}")   
print(f"Characters from index 5 to the end in reverse order: {name[5::-1]}")
print(f"Characters from index 0 to index 5 in reverse order with a step of 2: {name[0:5:-2]}")
print(f"Characters from index 5 to index 0 in reverse order with a step of 2: {name[5:0:-2]}")
print(f"Characters from index 5 to the end in reverse order with a step of 2: {name[5::-2]}")   
print(f"The last character of the string is: {name[-1]}")
print(f"The second to last character of the string is: {name[-2]}")
print(f"The third to last character of the string is: {name[-3]}")
print(f"The fourth to last character of the string is: {name[-4]}")
print(f"The fifth to last character of the string is: {name[-5]}")
print(f"the last four characters of the string are: {name[-4:]}")
print(f"the last five characters of the string are: {name[-5:]}")
print(f"the last six characters of the string are: {name[-6:]}")    
print(f"the last seven characters of the string are: {name[-7:]}")
print(f"the last eight characters of the string are: {name[-8:]}")  
