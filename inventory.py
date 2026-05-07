# Inventory Management System using Insertion Sort

def insertion_sort_inventory(inventory):
    # Sort inventory by quantity (lowest to highest)
    for i in range(1, len(inventory)):
        current_item = inventory[i]
        j = i - 1

        while j >= 0 and inventory[j]["quantity"] > current_item["quantity"]:
            inventory[j + 1] = inventory[j]
            j -= 1

        inventory[j + 1] = current_item

    return inventory


def display_inventory(inventory):
    print("\nCurrent Inventory:")
    print("-" * 40)

    for item in inventory:
        print(f"{item['name']:15} Quantity: {item['quantity']}")

    print("-" * 40)


def update_inventory(inventory):
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))

    # Check if item already exists
    found = False

    for item in inventory:
        if item["name"].lower() == item_name.lower():
            item["quantity"] = quantity
            found = True
            print(f"{item_name} updated successfully!")
            break

    # If item does not exist, add it
    if not found:
        inventory.append({
            "name": item_name,
            "quantity": quantity
        })
        print(f"{item_name} added to inventory!")

    # Re-sort inventory after update
    insertion_sort_inventory(inventory)


# Initial inventory
inventory = [
    {"name": "Laptops", "quantity": 12},
    {"name": "Keyboards", "quantity": 5},
    {"name": "Monitors", "quantity": 8},
    {"name": "Mice", "quantity": 20},
    {"name": "Headphones", "quantity": 3}
]

# Main program loop
while True:
    print("\nInventory Management System")
    print("1. Display Inventory")
    print("2. Update/Add Item")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        display_inventory(inventory)

    elif choice == "2":
        update_inventory(inventory)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
