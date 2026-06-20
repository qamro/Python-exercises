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

# PGCD function


def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(f"The PGCD of 12 and 18 is : {pgcd(12, 18)}")
print(f"The PGCD of 48 and 60 is : {pgcd(48, 60)}")
        
# absolute value function

def abs(x):
    if x > 0:
        return x
    else:
        return -x
    
print(f"The absolute value of -5 is : {abs(-5)}")
print(f"The absolute value of 10 is : {abs(10)}")

# cube function

def cube(x):
    return x*x*x

print(f"The cube of 3 is : {cube(3)}")
print(f"The cube of 4 is : {cube(4)}")

# decTObin function

def decTObin(n):
    if n == 0:
        return "0"
    
    result = ""
    while n > 0:
        bit = n % 2
        result = str(bit) + result
        n = n // 2
    
    return result
            
print(f"The binary representation of 2 is : {decTObin(2)}")   
print(f"The binary representation of 10 is : {decTObin(10)}")                  