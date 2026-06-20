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

# factorial function

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result = result * i
        
    return result

print(f"The factorial of 5 is : {factorial(5)}")
print(f"The factorial of 7 is : {factorial(7)}")