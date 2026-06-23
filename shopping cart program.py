foods = []
prices = []
total = 0
while True:     #an infinite loop that will keep asking the user to enter the food and price until the user enters 'q' to quit
    food = input("Enter the food to buy (enter 'q' to quit): ")
    if food.lower() == 'q':
        break    #exit the loop
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)
        total = total + price
print()   #for printing a new line
print("--------Your Shopping Cart--------")
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]:.2f}")
print(f"Total: ${total:.2f}")