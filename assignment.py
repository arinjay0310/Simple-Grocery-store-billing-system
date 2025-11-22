# Simple Grocery Store Billing System

items = {
    "Milk": 60,
    "Chips": 30,
    "Juice": 25,
    "Sugar": 45,
    "Rice": 120
    "Cold Drink": 70,
    "Tomato": 140,
}

print("---- GROCERY STORE MENU ----")
for item, price in items.items():
    print(f"{item} : ₹{price}")

cart = {}


n = int(input("\nHow many different items do you want to buy? "))

for i in range(n):
    name = input("\nEnter item name: ").capitalize()

    if name not in items:
        print("Item not available!")
        continue

    qty = int(input("Enter quantity: "))

    cart[name] = qty


print("\n------ BILL ------")
total = 0

for item, qty in cart.items():
    price = items[item]
    cost = price * qty
    total += cost
    print(f"{item} x {qty} = ₹{cost}")

gst = total * 0.05
grand_total = total + gst


print("------------------")
print(f"Subtotal : ₹{total}")
print(f"GST 5%   : ₹{gst}")
print(f"Total    : ₹{grand_total}")
print("------------------")