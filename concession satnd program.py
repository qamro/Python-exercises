menu = {"pizza": 3.00,
"tacos": 2.50,
"shawarma": 2.00,
"popcorn": 4.00,
"fries": 2.25,
"chips": 1.00,
"cereals": 1.50,
"yogurt": 0.50,
"soda": 1.25,
"lemonade": 1.75}
cart = []
total = 0
print("--------------MENU--------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------------------")    
while True:
    food = input("Select an item to buy: ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not 
    