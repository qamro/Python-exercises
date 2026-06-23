#dictionaries are ordered and changeable
#dictionaries are a type of collections just like lists, sets and tuples
#that is the the form of a dictionaries {"key: value","key: value"}



#these are dictionaries methods
countries = {"USA": "WASHINGTON DC","GERMANY": "BERLIN","ALGERIA": "ALGIERS"}
#the length of a dictionary
print(f"the length of the dictionary is: {len(countries)}")
#to get a value of any key
algeria_key = countries.get("ALGERIA")
print(algeria_key)
#check if a value exists or not (if a value doesn't exist it will return None)
if countries.get("CHINA"):
    print("The capital of china exists")
else:
    print("The capital of china doesn't exist") 
#update a current key value pair or add another one at the end
countries.update({"ALGERIA": "DJELFA"})    #update a current key value pair
countries.update({"INDIA": "NEW DELHI"})   #add a key value pair at the end
print(countries)       
#remove a key value pair using the key
countries.pop("USA")
print(countries)
##remove that last key value pair in the dictionary
countries.popitem()
print(countries)
#get a list of all keys of the dictionary
keys = countries.keys()
print(keys) #that shows a list of all keys
for key in countries.keys():    #if you want to show all the keys separately
    print(key)
#get a list of all values of the dictionary
values = countries.values()
print(values) #that shows a list of all keys
for value in countries.values():    #if you want to show all the values separately
    print(value)    
#get all the key value pairs as a list of a tuple(2D) 
items = countries.items()
print(items)
for key, value in countries.items():    #if you want to show all the key value pairs separately
    print(key, "->", value) 
#remove all the key value pairs in the dictionary
countries.clear()
print (countries)      