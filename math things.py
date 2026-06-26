import math

# circle things 
radius = float(input("Enter the radius of the circle: "))

area = math.pi * math.pow(radius, 2)
print(f"The area of the circle is: {round(area)}")  # round functions is used to round values

circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {round(circumference, 2)}")   # round values by 2 decimal numbers

# square things
side1 = float(input("Enter the side length of the square: "))
area1 = math.pow(side1, 2)
print(f"The area of the square is: {round(area1, 2)}") 

circumference = 4 * side1
print(f"The circumference of the square is: {round(circumference, 2)}")       

# pythagorean theorem
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print(f"The length of side c is: {c}")

# e and pi constants
print(math.e)
print(math.pi)