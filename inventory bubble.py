# Inventory Management System using Bubble Sort

def bubble_sort_inventory(inventory):
    # Sort inventory by quantity (lowest to highest)
    n = len(inventory)
    
    for i in range(n):
        # Flag to optimize: if no swaps, list is already sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent items
            if inventory[j]["quantity"] > inventory[j + 1]["quantity"]:
                # Swap if out of order
                inventory[j], inventory[j + 1] = inventory[j + 1], inventory[j]
                swapped = True
        
        # If no swapping occurred, list is sorted
        if not swapped:
            break
    
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
    bubble_sort_inventory(inventory)


# Initial inventory
inventory = [
    {"name": "Laptops", "quantity": 12},
    {"name": "Keyboards", "quantity": 5},
    {"name": "Monitors", "quantity": 8},
    {"name": "Mice", "quantity": 20},
    {"name": "Headphones", "quantity": 3}
]

# Sort initial inventory
bubble_sort_inventory(inventory)

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
