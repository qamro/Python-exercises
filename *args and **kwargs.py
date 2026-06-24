# =============================================================================
# SECTION 0: WHY DO WE EVEN NEED *args AND **kwargs?
# =============================================================================

# Normally, a function has a FIXED number of parameters:
def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(3, 5))   # 8  ✅
# print(add_two_numbers(3, 5, 7))  # ❌ TypeError: takes 2 positional arguments but 3 were given

# But what if you don't know HOW MANY arguments the user will pass?
# What if sometimes they pass 2 numbers, sometimes 10, sometimes 100?
# That's EXACTLY the problem *args and **kwargs solve.

print("\n" + "="*60)
print("SECTION 1: *args — Variable Positional Arguments")
print("="*60)

# =============================================================================
# SECTION 1: *args
# =============================================================================

# The * symbol tells Python:
# "Collect ALL extra positional arguments into a TUPLE and call it args"
# NOTE: the name "args" is just a convention, the * is what matters.

def my_first_args(*args):
    print(f"args = {args}")          # it's a regular tuple
    print(f"type = {type(args)}")    # <class 'tuple'>
    print(f"length = {len(args)}")

print("\n--- Calling with different number of arguments ---")
my_first_args()                         # args = ()         → empty tuple
my_first_args(1)                        # args = (1,)
my_first_args(1, 2, 3)                  # args = (1, 2, 3)
my_first_args("a", "b", "c", "d", "e") # args = ('a', 'b', 'c', 'd', 'e')


# --- EXAMPLE 1: Sum any number of numbers ---
def sum_all(*args):
    # args is a tuple, so we can loop over it, use sum(), len(), etc.
    total = 0
    for number in args:
        total += number
    return total

print("\n--- Example 1: Sum any number of numbers ---")
print(sum_all(1, 2))           # 3
print(sum_all(1, 2, 3))        # 6
print(sum_all(10, 20, 30, 40)) # 100
print(sum_all())               # 0  → empty tuple, loop never runs


# --- EXAMPLE 2: Print all items with their index ---
def print_with_index(*args):
    for index, value in enumerate(args):
        print(f"  [{index}] → {value}")

print("\n--- Example 2: Print items with index ---")
print_with_index("apple", "banana", "cherry")
# [0] → apple
# [1] → banana
# [2] → cherry


# --- EXAMPLE 3: Find the maximum value ---
def find_max(*args):
    if len(args) == 0:
        return None  # can't find max of nothing
    max_val = args[0]       # start with the first element
    for num in args:
        if num > max_val:
            max_val = num
    return max_val

print("\n--- Example 3: Find max among any number of values ---")
print(find_max(3, 1, 9, 2, 7))    # 9
print(find_max(100, 200, 50))      # 200
print(find_max(42))                # 42


# --- EXAMPLE 4: Combining *args WITH normal parameters ---
# RULE: normal parameters come FIRST, *args come AFTER
def greet_people(greeting, *args):
    # "greeting" takes the first argument normally
    # *args takes everything else
    for name in args:
        print(f"  {greeting}, {name}!")

print("\n--- Example 4: *args with normal parameters ---")
greet_people("Hello", "Alice", "Bob", "Charlie")
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!

greet_people("Good morning", "Diana")
# Good morning, Diana!


# --- EXAMPLE 5: Using *args to build a sentence ---
def build_sentence(*words):
    sentence = " ".join(words)  # join() works perfectly on tuples
    return sentence + "."

print("\n--- Example 5: Build a sentence from words ---")
print(build_sentence("The", "cat", "sat", "on", "the", "mat"))
# The cat sat on the mat.
print(build_sentence("Python", "is", "awesome"))
# Python is awesome.


# --- EXAMPLE 6: Passing a list INTO *args using unpacking ---
# You can "unpack" a list/tuple when calling a function using *
numbers = [5, 10, 15, 20]
print("\n--- Example 6: Unpacking a list into *args ---")
print(sum_all(*numbers))   # same as sum_all(5, 10, 15, 20) → 50

coordinates = (3, 7, 1)
print(find_max(*coordinates))  # same as find_max(3, 7, 1) → 7


print("\n" + "="*60)
print("SECTION 2: **kwargs — Variable Keyword Arguments")
print("="*60)

# =============================================================================
# SECTION 2: **kwargs
# =============================================================================

# The ** symbol tells Python:
# "Collect ALL extra keyword arguments into a DICTIONARY and call it kwargs"
# Keyword arguments = arguments passed as key=value
# NOTE: "kwargs" is just a convention, the ** is what matters.

def my_first_kwargs(**kwargs):
    print(f"kwargs = {kwargs}")       # it's a regular dict
    print(f"type = {type(kwargs)}")   # <class 'dict'>
    print(f"keys = {list(kwargs.keys())}")

print("\n--- Calling with different keyword arguments ---")
my_first_kwargs()
# kwargs = {}

my_first_kwargs(name="Alice")
# kwargs = {'name': 'Alice'}

my_first_kwargs(name="Alice", age=30, city="New York")
# kwargs = {'name': 'Alice', 'age': 30, 'city': 'New York'}


# --- EXAMPLE 7: Display user profile ---
def display_profile(**kwargs):
    print("  --- User Profile ---")
    for key, value in kwargs.items():  # .items() gives key-value pairs
        print(f"  {key.capitalize()}: {value}")

print("\n--- Example 7: Display user profile ---")
display_profile(name="Bob", age=25, job="Developer", city="London")
# Name: Bob
# Age: 25
# Job: Developer
# City: London


# --- EXAMPLE 8: **kwargs with normal parameters ---
# RULE: normal parameters first, then **kwargs last
def create_account(username, **kwargs):
    print(f"\n  Creating account for: {username}")
    print(f"  Extra info provided:")
    for key, value in kwargs.items():
        print(f"    - {key}: {value}")

print("\n--- Example 8: **kwargs with normal parameter ---")
create_account("john_doe", email="john@example.com", age=28, country="USA")
# Creating account for: john_doe
# Extra info provided:
#   - email: john@example.com
#   - age: 28
#   - country: USA


# --- EXAMPLE 9: Accessing specific keys from **kwargs ---
def introduce_person(**kwargs):
    # You can access kwargs just like a normal dictionary
    name = kwargs.get("name", "Unknown")   # .get() with a default value
    age  = kwargs.get("age", "?")
    job  = kwargs.get("job", "unemployed")
    print(f"  Hi! I'm {name}, {age} years old, working as a {job}.")

print("\n--- Example 9: Accessing specific keys from kwargs ---")
introduce_person(name="Sara", age=22, job="designer")
# Hi! I'm Sara, 22 years old, working as a designer.

introduce_person(name="Mike")
# Hi! I'm Mike, ? years old, working as a unemployed.
# (missing keys use the default values from .get())


# --- EXAMPLE 10: Unpacking a dict INTO **kwargs using ** ---
person_info = {"name": "Emma", "age": 35, "job": "scientist"}
print("\n--- Example 10: Unpacking a dict into **kwargs ---")
introduce_person(**person_info)
# same as introduce_person(name="Emma", age=35, job="scientist")


# --- EXAMPLE 11: Build a CSS-style config string ---
def build_style(**kwargs):
    parts = []
    for prop, val in kwargs.items():
        css_prop = prop.replace("_", "-")  # font_size → font-size
        parts.append(f"{css_prop}: {val}")
    return "; ".join(parts)

print("\n--- Example 11: Build style string from kwargs ---")
style = build_style(color="red", font_size="16px", background_color="white")
print(f"  Style: {style}")
# Style: color: red; font-size: 16px; background-color: white


print("\n" + "="*60)
print("SECTION 3: *args AND **kwargs TOGETHER")
print("="*60)

# =============================================================================
# SECTION 3: *args AND **kwargs TOGETHER
# =============================================================================

# You can use BOTH in the same function.
# THE ORDER IS MANDATORY:
#   1. Normal parameters
#   2. *args
#   3. **kwargs

# def my_func(normal, *args, **kwargs)  ✅ correct
# def my_func(**kwargs, *args)          ❌ SyntaxError


# --- EXAMPLE 12: All three together ---
def show_everything(title, *args, **kwargs):
    print(f"\n  Title: {title}")
    print(f"  Positional extras (args): {args}")
    print(f"  Keyword extras (kwargs):  {kwargs}")

print("\n--- Example 12: All three together ---")
show_everything("My Report", "item1", "item2", author="Alice", year=2024)
# Title: My Report
# Positional extras (args): ('item1', 'item2')
# Keyword extras (kwargs):  {'author': 'Alice', 'year': 2024}


# --- EXAMPLE 13: Build an order receipt ---
def create_order(customer_name, *items, **options):
    print(f"\n  Order for: {customer_name}")
    print(f"  Items ordered:")
    for item in items:
        print(f"    🛒 {item}")
    print(f"  Options:")
    for key, val in options.items():
        print(f"    {key}: {val}")

print("\n--- Example 13: Order receipt ---")
create_order(
    "John",
    "Pizza", "Burger", "Fries",
    delivery=True,
    payment="credit card",
    tip="15%"
)
# Order for: John
# Items:  Pizza, Burger, Fries
# Options: delivery: True, payment: credit card, tip: 15%


# --- EXAMPLE 14: A mini logging system ---
def log(level, *messages, **context):
    print(f"\n  [{level.upper()}]")
    for msg in messages:
        print(f"    > {msg}")
    if context:
        print(f"    Context: {context}")

print("\n--- Example 14: Mini logger ---")
log("info", "Server started", "Listening on port 8080")
log("error", "Database connection failed", host="localhost", port=5432)
log("warning", "Low memory", "Disk almost full", server="prod-01", alert=True)


print("\n" + "="*60)
print("SECTION 4: UNPACKING — The * and ** Outside Functions")
print("="*60)

# =============================================================================
# SECTION 4: UNPACKING WITH * AND **
# =============================================================================

# The * and ** can also be used OUTSIDE of function definitions
# to unpack iterables and dictionaries.


# --- EXAMPLE 15: Unpacking lists with * ---
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = [*list1, *list2]  # merge two lists
print(f"\n--- Example 15: Merging lists with * ---")
print(combined)  # [1, 2, 3, 4, 5, 6]

# Add extra elements too:
extended = [0, *list1, 99, *list2, 100]
print(extended)  # [0, 1, 2, 3, 99, 4, 5, 6, 100]


# --- EXAMPLE 16: Unpacking dicts with ** ---
defaults   = {"theme": "dark", "language": "en", "font_size": 14}
overrides  = {"font_size": 18, "language": "ar"}

merged = {**defaults, **overrides}  # later keys OVERRIDE earlier ones
print(f"\n--- Example 16: Merging dicts with ** ---")
print(merged)
# {'theme': 'dark', 'language': 'ar', 'font_size': 18}
# Note: font_size and language were overridden by the second dict


# --- EXAMPLE 17: Unpacking when calling functions ---
def power(base, exponent):
    return base ** exponent

args_tuple = (2, 10)
print(f"\n--- Example 17: Unpacking when calling functions ---")
print(power(*args_tuple))      # same as power(2, 10) → 1024

kwargs_dict = {"base": 3, "exponent": 4}
print(power(**kwargs_dict))    # same as power(base=3, exponent=4) → 81


# --- EXAMPLE 18: Collect the "rest" of a list ---
first, *rest = [10, 20, 30, 40, 50]
print(f"\n--- Example 18: Collect the rest ---")
print(f"first = {first}")  # 10
print(f"rest  = {rest}")   # [20, 30, 40, 50]

first, *middle, last = [1, 2, 3, 4, 5]
print(f"first  = {first}")   # 1
print(f"middle = {middle}")  # [2, 3, 4]
print(f"last   = {last}")    # 5


print("\n" + "="*60)
print("SECTION 5: REAL WORLD USE CASES")
print("="*60)

# =============================================================================
# SECTION 5: REAL WORLD USE CASES
# =============================================================================


# --- USE CASE 1: Wrapper / Decorator-style function ---
# Very common pattern: a function that wraps another function
def run_with_logging(func, *args, **kwargs):
    print(f"\n  Calling function: {func.__name__}")
    print(f"  With args:   {args}")
    print(f"  With kwargs: {kwargs}")
    result = func(*args, **kwargs)
    print(f"  Result: {result}")
    return result

def multiply(x, y):
    return x * y

def greet(name, loud=False):
    msg = f"Hello, {name}!"
    return msg.upper() if loud else msg

print("\n--- Use Case 1: Wrapper function ---")
run_with_logging(multiply, 6, 7)
run_with_logging(greet, "Alice", loud=True)


# --- USE CASE 2: Configuration builder ---
def configure_server(host, port, **options):
    config = {
        "host": host,
        "port": port,
        **options   # merge extra options right into the dict!
    }
    return config

print("\n--- Use Case 2: Config builder ---")
cfg = configure_server(
    "localhost", 8080,
    debug=True,
    max_connections=100,
    timeout=30,
    ssl=False
)
for k, v in cfg.items():
    print(f"  {k}: {v}")


# --- USE CASE 3: Flexible data formatter ---
def format_table(*rows, **style):
    separator = style.get("separator", " | ")
    header    = style.get("header", True)

    if header and rows:
        print("  " + separator.join(str(cell) for cell in rows[0]))
        print("  " + "-" * 40)
        data_rows = rows[1:]
    else:
        data_rows = rows

    for row in data_rows:
        print("  " + separator.join(str(cell) for cell in row))

print("\n--- Use Case 3: Flexible table formatter ---")
format_table(
    ("Name", "Age", "City"),
    ("Alice", 30, "New York"),
    ("Bob",   25, "London"),
    ("Carol", 35, "Paris"),
    separator=" | ",
    header=True
)


# --- USE CASE 4: Chaining / passing args through multiple functions ---
# This is VERY common in real code: passing args from one function to another
def inner_function(a, b, c):
    return f"a={a}, b={b}, c={c}"

def outer_function(*args, **kwargs):
    # outer doesn't care about the args, just passes them along
    print("  Outer function called, forwarding to inner...")
    return inner_function(*args, **kwargs)

print("\n--- Use Case 4: Forwarding args to another function ---")
result = outer_function(1, 2, c=3)
print(f"  Result: {result}")


# --- USE CASE 5: Simulate a database query builder ---
def query(table, *fields, **filters):
    selected = ", ".join(fields) if fields else "*"
    sql = f"SELECT {selected} FROM {table}"
    if filters:
        conditions = " AND ".join(f"{k} = '{v}'" for k, v in filters.items())
        sql += f" WHERE {conditions}"
    return sql + ";"

print("\n--- Use Case 5: SQL query builder ---")
print(query("users"))
# SELECT * FROM users;

print(query("users", "name", "email"))
# SELECT name, email FROM users;

print(query("users", "name", "email", age=25, city="Paris"))
# SELECT name, email FROM users WHERE age = '25' AND city = 'Paris';

print(query("products", price=99, in_stock=True))
# SELECT * FROM products WHERE price = '99' AND in_stock = 'True';



print("\n" + "="*60)
print("SECTION 7: QUICK REFERENCE CHEAT SHEET")
print("="*60)

cheatsheet = """
  ┌─────────────────────────────────────────────────────────┐
  │               *args and **kwargs CHEAT SHEET            │
  ├──────────────┬──────────────────────────────────────────┤
  │              │  *args               │  **kwargs          │
  ├──────────────┼──────────────────────┼────────────────────┤
  │ Type         │  tuple               │  dict              │
  │ Syntax       │  *args               │  **kwargs          │
  │ Passed as    │  positional          │  key=value         │
  │ Example call │  f(1, 2, 3)          │  f(a=1, b=2)       │
  │ Access       │  args[0], loop       │  kwargs['k'], loop │
  │ Order        │  2nd                 │  always LAST       │
  │ Unpack with  │  *my_list            │  **my_dict         │
  └──────────────┴──────────────────────┴────────────────────┘

  PARAMETER ORDER IN FUNCTION DEFINITION:
  def func(normal_params, *args, keyword_only_params, **kwargs)
             ↑                   ↑                      ↑
           First               Second                  Last
"""
print(cheatsheet)

