menu = {
    "Pizza": 70,
    "Pasta": 50,
    "Burger": 30,
    "Salad": 30,
    "Coffee": 60,
    "Fries": 20,
    "Kabab": 60,
}

print(" Hello sir, Welcome to our restaurant. Here is our menu:\n")
print("Pizza: 70TK/-\nPasta: 50TK/-\nBurger: 30TK/-\nSalad: 30Tk/-\nCoffee: 60TK/-\nFries: 20Tk/-\nkabab: 60Tk/-")
order_total = 0
order_details = {}
while True:
    item = input("\nEnter the item you want to order: ").strip().capitalize()

    if item in menu:
        try:
            quantity = int(input(f"How many {item}s would you like to order? "))
            if quantity > 0:
                cost = menu[item] * quantity
                order_total += cost
                order_details[item] = order_details.get(item, 0) + quantity
                print(f"{quantity} x {item} added to your order.")
            else:
                print("Please enter a valid quantity.")
        except ValueError:
            print("Please enter a number for quantity.")
    else:
        print(" Sorry! That item is not available.")

    another = input("Would you like to order anything else? (Yes/No): ").strip().lower()
    if another != 'yes':
        break

print("\n Thanks for your order, sir.")
print("Here is your bill:\n")
for item, quantity in order_details.items():
    print(f"{item} x {quantity} = {menu[item] * quantity} TK")

print(f"\nTotal Amount to Pay: {order_total} TK")

