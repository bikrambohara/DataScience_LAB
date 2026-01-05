# 4. Inventory Tracker
# Imagine a small store inventory like {"apple": 10, "banana": 5, "milk": 2}. Program should allow
# adding new items, selling items (subtract quantity), and print items that are low in stock (<3).

inventory = {}

items = input("Enter items (apple-4 rice-5 milk-9): ")

item_list = items.split()

for item in item_list:
    name, qty = item.split("-")
    inventory[name] = int(qty)

print("Current Inventory:")
for item, qty in inventory.items():
    print(f"{item}: {qty}")


while True:
    print("\n1. Add items")
    print("2. Sell items")
    print("3. Show low stock items (<3)")
    print("4. Show inventory")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter item name: ")
        qty = int(input("Enter quantity to add: "))

        if name in inventory:
            inventory[name] += qty
        else:
            inventory[name] = qty

    elif choice == 2:
        name = input("Enter item name to sell: ")
        qty = int(input("Enter quantity to sell: "))

        if name in inventory and inventory[name] >= qty:
            inventory[name] -= qty
        elif qty<get.inventory("qty"):
            print("Not enough stock")
        else:
            print("Item not found")

    elif choice == 3:
        print("Low stock items:")
        for item, qty in inventory.items():
            if qty < 3:
                print(f"{item}:{qty}")
            else:
                print("No low stock items")

    elif choice == 4:
        print("Current Inventory:")
        for item, qty in inventory.items():
            if qty ==0:
                print("No item to show")
            else:
                print(f"{item}: {qty}")

    elif choice == 5:
        break

    else:
        print("Invalid choice")