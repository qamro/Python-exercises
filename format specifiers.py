#format specifiers 
 
name = "qamro"
age = 18
height = 1.753  
grade = -3.53435
print(f"My name is {name}, I am {age} years old and my height is {height} meters.")
print("My name is {}, I am {} years old and my height is {} meters.".format(name, age, height))     
print("My name is {0}, I am {1} years old and my height is {2} meters.".format(name, age, height))
print("My name is {name}, I am {age} years old and my height is {height} meters.".format(name=name, age=age, height=height)) 
print(f"My name is {name}, I am {age} years old and my height is {height:.2f} meters.")     
print("My name is {}, I am {} years old and my height is {:.2f} meters.".format(name, age, height))
print("My name is {0}, I am {1} years old and my height is {2:.2f} meters.".format(name, age, height))
print("My name is {name}, I am {age} years old and my height is {height:.2f} meters.".format(name=name, age=age, height=height))        
print(f"My name is {name}, I am {age} years old and my height is {height:.2f} meters and my grade is {grade:.2f}.")
print("My name is {}, I am {:+.2f} years old and my height is {:+.2f} meters and my grade is {:+.2f}.".format(name, age, height, grade))
print("My name is {0}, I am {1:+.2f} years old and my height is {2:+.2f} meters and my grade is {3:+.2f}.".format(name, age, height, grade))
print("My name is {name}, I am {age:+.2f} years old and my height is {height:+.2f} meters and my grade is {grade:+.2f}.".format(name=name, age=age, height=height, grade=grade))    



value = 12345.67890
value2 = -12345.67890
print(f"Value: {value:.2f}")
print(f"Value: {value:.3f}")
print(f"Value: {value:.4f}")
print(f"Value: {value:.5f}")
print(f"Value: {value:.6f}")
print(f"Value: {value:^20}")
print(f"Value: {value:>20}")
print(f"Value: {value:<20}")
print(f"Value: {value:,.2f}")
print(f"Value: {value2:,.2f}")
print(f"Value: {value:,}")
print(f"Value: {value:020.2f}")
print(f"Value: {value2:020.2f}")    
