# exception is an event that interrupts the normal flow of a program's execution.
# It is an error that occurs during the execution of a program
# Types of exceptions include: ZeroDivisionError, FileNotFoundError, ValueError, TypeError, IndexError, KeyError, etc.
"""
the structure of exception handling in python is as follows:
try:
    # code that may raise an exception
except ExceptionType:
    # code that runs if an exception occurs
else:
    # code that runs if no exception occurs
finally:
    # code that runs regardless of whether an exception occurs or not
    
"""

# Example of exception handling in python
number = int(input("Enter a number: "))
try:
    result = 10 / number
except ZeroDivisionError:
    print("Error: Cannot divide by zero piece of shit.")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")    