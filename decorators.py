# decorators are used to modify the behavior of functions or methods. 
# they are basically functions that take another function as an argument and extend or alter its behavior without explicitly modifying it.

def my_first_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

def my_second_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        func(*args, **kwargs)
        print("After the function is called.")
    return wrapper

@my_first_decorator
@my_second_decorator
def say_hello(name):
    print(f"Hello, {name}!")




# example usage

say_hello("Qamro")


"""
well here i will explain how the decorators work in this code.
we use @my_first_decorator and @my_second_decorator to decorate the say_hello function.
When we call say_hello("Qamro"), the following happens:
1. The say_hello function is passed to my_second_decorator, which returns the wrapper function defined inside it.
2. The wrapper function from my_second_decorator is then passed to my_first_decorator, which returns the wrapper function defined inside it.
3. Finally, when we call say_hello("Qamro"), it shows:
        Something is happening before the function is called.
        Before the function is called.
        Hello, Qamro!
        After the function is called.
        Something is happening after the function is called.
"""

"""
we use wrapper functions to wrap the original function and add additional behavior before and after the function call.
if we dont use it and just write the code like that :
        def my_first_decorator(func):
            print("Something is happening before the function is called.")
            func(*args, **kwargs)
            print("Something is happening after the function is called.")

it will work whether we call the function or not because the decorator will be executed at the time of decoration, not at the time of function call.
"""

"""
and we used *args and **kwargs as a parameters of wrapper and func functions to accept any arguments from the main function whether its args or kwargs
"""