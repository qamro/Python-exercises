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
        bin = n % 2
        result = str(bin) + result
        n = n // 2
    
    return result
            
print(f"The binary representation of 2 is : {decTObin(2)}")   
print(f"The binary representation of 10 is : {decTObin(10)}")    

# prime function

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
        
print(f"Is 7 a prime number? : {is_prime(7)}")
print(f"Is 10 a prime number? : {is_prime(10)}")        

                 
# sum of digits function

def sum_of_digits(n):
    sum = 0
    while n > 0:
        r = n % 10
        sum = sum + r
        n = n // 10

    return sum

print(f"The sum of digits of 123 is : {sum_of_digits(123)}")
print(f"The sum of digits of 456 is : {sum_of_digits(456)}")

#binTOdec function

def binTOdec(n):
    
    if n not in (0, 1):
        return "Invalid binary number"

    decimal = 0
    p = 0
    while n > 0:
        r = n % 10
        decimal = decimal + r * power(2, p)
        n = n // 10
        p = p + 1

    return decimal

print(f"The decimal representation of 1010 is : {binTOdec(1010)}")
print(f"The decimal representation of 1111 is : {binTOdec(1111)}")
print(f"The decimal representation of 10010011 is : {binTOdec(10010011)}")
print(f"The decimal representation of 12324 is : {binTOdec(12324)}")


# perfect number function

def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i

    if sum == n:
        return True
    else:
        return False
    
    
print(f"Is 6 a perfect number? : {is_perfect(6)}")
print(f"Is 28 a perfect number? : {is_perfect(28)}")    

# armstrong number function

def is_armstrong(n):
    num_digits = len(str(n))
    sum = 0
    temp = n


    while temp > 0:
        r = temp % 10
        sum = sum + power(r, num_digits)
        temp = temp // 10

    if sum == n:
        return True
    else:
        return False  
    
    
print(f"Is 153 an armstrong number? : {is_armstrong(153)}")
print(f"Is 9474 an armstrong number? : {is_armstrong(9474)}")