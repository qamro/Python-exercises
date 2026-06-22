import math

# circle things 
radius = float(input("Enter the radius of the circle: "))

area = math.pi * math.pow(radius, 2)
print(f"The area of the circle is: {area}")

circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {math.round(circumference, 2)}")

# square things
side = float(input("Enter the side length of the square: "))
area = math.pow(side, 2)
print(f"The area of the square is: {math.round(area, 2)}") 

circumference = 4 * side
print(f"The circumference of the square is: {math.round(circumference, 2)}")       

# pythagorean theorem
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print(f"The length of side c is: {c}")

