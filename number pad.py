#we are gonna use a 2D tuple 
#just to know there are 2D lists and 2D sets
num_pad = ((1,2,3),(4,5,6),(7,8,9,),("*",0,"#"))   # thats 2D tuple
for row in num_pad:
    for num in row:
        print(num, end=" ")
    
    print()    #just to add new line for the next row