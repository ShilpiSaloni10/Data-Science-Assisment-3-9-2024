# Input Function 
pizzas = int(input("Enter the no of pizzas bought: "))
puffs = int(input("Enter the no of puffs bought: "))
cold_drinks = int(input("Enter the no of cold_drinks bought: "))

# Menu_Price
pizza_price = 100
puff_price = 20
cold_drinks_price = 10

# Calculating total price
total_price = (pizzas * pizza_price) + (puffs * puff_price) + (cold_drinks * cold_drinks_price)

print("\nBill Details")
print("No of pizzas:", pizzas)
print("No of puffs:", puffs)
print("No of cooldrinks:", cold_drinks)
print("Total price =", total_price)

