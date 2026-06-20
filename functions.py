# square function

def square(x):
    return x*x

print(f"the square of 6 is : {square(6)}")
print(f"The square of the 9 is : {square(9)}")

# power function

def power(x, y):
    result = 1
    for i in range(y):
        result = result * x
    return result
    
print(f"The power of 2 to the 3 is : {power(2,3)}")
print(f"The power of 3 to the 4 is : {power(3,4)}")

