# Define the manu of restaurent

menu = {
    "Pizza" : 199,
    "Pasta" : 149,
    "Burger" : 149,
    "Salad" : 179,
    "Coffe" : 99,
}

# Greet

print("Welcome to PYTHON Restaurant")
print("Our Menu Have")
print("Pizza: 199\nPasta: 149\nBurger: 149\nSalad: 179\nCoffe: 99")

order_total = 0

item_1 = input("Enter the name what you want to order : ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order ")
else:
    print("Order somethin that we can serve to you")

another_order = input("Do ypu want to add semething else in your order? [Yes/No] : ")
if another_order == "Yes":
    item_2 = input("Enter the name of the second item : ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available")

print(f"The total amount of order is {order_total}")
