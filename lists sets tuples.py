#lists [] changeable, ordered, allows duplicates
#sets {} changeable, unordered, no duplicates
#tuples () unchangeable, ordered, allows duplicates


#now we start with lists methods
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits)
#len() method returns the number of elements in the list
length = len(fruits)
print(f"Length of fruits list: {length}")
#check if an element is present in the list
print("banana" in fruits)
#append() method adds an element to the end of the list
fruits.append("grape")      
print(fruits)
#insert() method adds an element at a specified position
fruits.insert(2, "pineapple")
print(fruits)
#remove() method removes the first occurrence of an element from the list
fruits.remove("banana")
print(fruits)
#pop() method removes the element at the specified position 
fruits.pop(1)
print(fruits)
#extend() method adds the elements of a list (or any iterable), to the end of the current list
fruits2 = ["pear", "peach", "plum"]
fruits.extend(fruits2)
print(fruits)
#index() method returns the index of the first occurrence of an element in the list
index = fruits.index("kiwi")
print(f"Index of kiwi: {index}")
#count() method returns the number of times an element appears in the list
count = fruits.count("apple")
print(f"Count of apple: {count}")
#sort() method sorts the list in ascending order
fruits.sort()
print(fruits)
#reverse() method reverses the order of the list
fruits.reverse()
print(fruits)   
#clear() method removes all the elements from the list
fruits.clear()
print(fruits)




#now we start with sets methods
fruits_set = {"apple", "banana", "cherry"}
print(fruits_set)
#len() method returns the number of elements in the set
length = len(fruits_set)
print(f"Length of fruits set: {length}")
#check if an element is present in the set
print(f"Is 'banana' in fruits_set? {'banana' in fruits_set}")
#add() method adds an element to the set    
fruits_set.add("orange")
print(fruits_set)
#remove() method removes an element from the set (if the element is not present, it raises a KeyError)
fruits_set.remove("banana")
print(fruits_set)
#discard() method removes an element from the set (if the element is not present, it does not raise an error)
fruits_set.discard("kiwi")  
print(fruits_set)   
#pop() method removes an element randomly 
fruits_set.pop()
print(fruits_set)
#union() method returns a new set with all the elements from both sets  
fruits_set2 = {"pear", "peach", "plum"}
fruits_set3 = fruits_set.union(fruits_set2)
print(fruits_set3)
#intersection() method returns a new set with only the elements that are common to both sets
fruits_set4 = fruits_set.intersection(fruits_set2)
print(fruits_set4)
#difference() method returns a new set with the elements that are in the first set but not in the second set
fruits_set5 = fruits_set.difference(fruits_set2)
print(fruits_set5)  
#symmetric_difference() method returns a new set with the elements that are in either of the sets, but not in both
fruits_set6 = fruits_set.symmetric_difference(fruits_set2)
print(fruits_set6)  
#issubset() method returns True if all the elements of the set are present in another set(the set is a subset of another set)
is_subset = fruits_set.issubset(fruits_set2)
print(f"Is fruits_set a subset of fruits_set2? {is_subset}")
#issuperset() method returns True if all the elements of another set are present in the set
#(the set is a superset of another set or the other set is a subset of the set)
is_superset = fruits_set.issuperset(fruits_set2)
print(f"Is fruits_set a superset of fruits_set2? {is_superset}")    
#clear() method removes all the elements from the set
fruits_set.clear()
print(fruits_set)   





#now we start with tuples methods (tuples are immutable, so we cannot change the original tuple)
fruits_tuple = ("apple", "banana", "cherry")
print(fruits_tuple)
#len() method returns the number of elements in the tuple
length = len(fruits_tuple)
print(f"Length of fruits tuple: {length}")
#check if an element is present in the tuple
print(f"Is 'banana' in fruits_tuple? {'banana' in fruits_tuple}")
#count() method returns the number of times an element appears in the tuple
count = fruits_tuple.count("apple")
print(f"Count of apple: {count}")
#index() method returns the index of the first occurrence of an element in the tuple
index = fruits_tuple.index("cherry")
print(f"Index of cherry: {index}")  
#tuple(sorted(name of original tuple)) method sorts the tuple in ascending order and returns a new tuple 
fruits_tuple2 = tuple(sorted(fruits_tuple))
print(fruits_tuple2)
#tuple(reversed(name of original tuple)) method reverses the order of the tuple and returns a new tuple 
fruits_tuple3 = tuple(reversed(fruits_tuple))
print(fruits_tuple3)    
#tuple(name of original tuple) method creates a new tuple from the original tuple 
fruits_tuple4 = tuple(fruits_tuple)
print(fruits_tuple4)
#tuple(name of original list) method creates a new tuple from a list
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple5 = tuple(fruits_list)
print(fruits_tuple5)
#tuple(name of original set) method creates a new tuple from a set
fruits_set = {"apple", "banana", "cherry"}
fruits_tuple6 = tuple(fruits_set)
print(fruits_tuple6)
#tuple(name of original string) method creates a new tuple from a string
fruits_string = "apple, banana, cherry" 
fruits_tuple7 = tuple(fruits_string)
print(fruits_tuple7)    
#create an empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")
#create a tuple with one element (we need to add a comma after the element)
one_element_tuple = ("apple",)
print(f"One element tuple: {one_element_tuple}")    
