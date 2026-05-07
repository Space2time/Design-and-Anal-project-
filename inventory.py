
class InventoryManager:

    def __init__(self):
        self.inventory = [
            {"name": "Laptops", "quantity": 12, "price": 999.99, "weight": 5.5, "type": "Electronics"},
            {"name": "Keyboards", "quantity": 5, "price": 49.99, "weight": 1.2, "type": "Accessories"},
            {"name": "Monitors", "quantity": 8, "price": 199.99, "weight": 8.5, "type": "Electronics"},
            {"name": "Mice", "quantity": 20, "price": 25.99, "weight": 0.5, "type": "Accessories"},
            {"name": "Headphones", "quantity": 3, "price": 79.99, "weight": 0.8, "type": "Audio"}
        ]

    # Helper: print a compact view of inventory showing only name and the sort key
    def _print_compact(self, sort_key, message=""):
        if message:
            print(message)
        print("  ", end="")
        for i, item in enumerate(self.inventory):
            print(f"[{i}]{item['name']}({item[sort_key]})  ", end="")
        print()

    # Insertion Sort Method with detailed process display
    def insertion_sort_inventory(self, sort_key):
        print(f"\n--- Starting Insertion Sort by '{sort_key}' (ascending) ---")
        print("Initial inventory:")
        self._print_compact(sort_key, "")

        n = len(self.inventory)

        for i in range(1, n):
            current_item = self.inventory[i]
            current_val = current_item[sort_key]
            print(f"\nPass {i}: Insert element '{current_item['name']}' (key = {current_val})")

            j = i - 1
            # Show comparisons and shifts
            while j >= 0 and self.inventory[j][sort_key] > current_val:
                print(f"   Comparing {current_item['name']}({current_val}) with {self.inventory[j]['name']}({self.inventory[j][sort_key]}) → shift right")
                self.inventory[j + 1] = self.inventory[j]
                j -= 1
                # Show temporary state after shift
                self._print_compact(sort_key, "   After shift:")

            # Insert current element at correct position
            self.inventory[j + 1] = current_item
            print(f"   Inserted '{current_item['name']}' at index {j+1}")
            self._print_compact(sort_key, "   Inventory after insertion:")

        print(f"\n--- Finished sorting by '{sort_key}' ---")
        self._print_compact(sort_key, "Final sorted inventory:")

    # Display full inventory (all fields) – unchanged
    def display_inventory(self):
        print("\nCurrent Inventory:")
        print("-" * 75)
        print(f"{'Name':15} {'Quantity':10} {'Price':10} {'Weight':10} {'Type':15}")
        print("-" * 75)
        for item in self.inventory:
            print(f"{item['name']:15} {item['quantity']:<10} ${item['price']:<9.2f} {item['weight']:<10} {item['type']:<15}")
        print("-" * 75)

    # Add or update inventory – unchanged
    def update_inventory(self):
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        weight = float(input("Enter weight: "))
        item_type = input("Enter item type: ")

        found = False
        for item in self.inventory:
            if item["name"].lower() == item_name.lower():
                item["quantity"] = quantity
                item["price"] = price
                item["weight"] = weight
                item["type"] = item_type
                found = True
                print(f"{item_name} updated successfully!")
                break

        if not found:
            new_item = {"name": item_name, "quantity": quantity, "price": price, "weight": weight, "type": item_type}
            self.inventory.append(new_item)
            print(f"{item_name} added successfully!")

    # Sorting menu – unchanged
    def sort_menu(self):
        print("\nSort Inventory By:")
        print("1. Quantity")
        print("2. Price")
        print("3. Weight")
        print("4. Type")
        choice = input("Choose sorting option: ")
        if choice == "1":
            self.insertion_sort_inventory("quantity")
        elif choice == "2":
            self.insertion_sort_inventory("price")
        elif choice == "3":
            self.insertion_sort_inventory("weight")
        elif choice == "4":
            self.insertion_sort_inventory("type")
        else:
            print("Invalid option.")

    # Main program loop – initially sorts by quantity (shows the process)
    def run(self):
        # Initial sort (shows step-by-step process)
        self.insertion_sort_inventory("quantity")

        while True:
            print("\nInventory Management System")
            print("1. Display Inventory")
            print("2. Update/Add Item")
            print("3. Sort Inventory")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.display_inventory()
            elif choice == "2":
                self.update_inventory()
            elif choice == "3":
                self.sort_menu()
            elif choice == "4":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")


# Create object and run program
inventory_system = InventoryManager()
inventory_system.run()
