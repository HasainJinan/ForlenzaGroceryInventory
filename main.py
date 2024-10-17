def add_item(inventory, name, price, quantity):
    """
    Add a new item to the inventory.
    
    Args:
    inventory (dict): The current inventory
    name (str): The name of the item
    price (str): The price of the item
    quantity (str): The quantity of the item
    """
    if name in inventory:
        choose = input("Are you sure you want to overwrite this item? Y/N: ")
        if choose == "Y":
            inventory[name] = {"price": price, "quantity": quantity}
            print(f"{name} added to the inventory.")
        elif choose == "N":
            pass
        else:
            print("Sorry I do not understand.")
    else:
        inventory[name] = {"price": price, "quantity": quantity}
        print(f"{name} added to the inventory.")

def remove_item(inventory, item_name):
    """
    Remove an item from the inventory.
    
    Args:
    inventory (dict): The current inventory
    item_name (str): The name of the item to remove
    """
    try:
        del inventory[item_name]
    except:
        print(item_name, " does not exist in the inventory.")
    else:
        print(f"{item_name} removed from the inventory.")

def update_quantity(item_name, new_quantity):
    """
    Update the quantity of an item in the inventory.
    
    Args:
    inventory (dict): The current inventory
    item_name (str): The name of the item to update
    new_quantity (str): The new quantity of the item
    """
    inventory[item_name] = {"quantity": new_quantity}
    print(f"{item_name} quantity updated to {new_quantity}.")

def display_inventory(inventory):
    """
    Display all items in the inventory.
    
    Args:
    inventory (dict): The current inventory
    """
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for name in inventory:
            item = inventory[name]
            print(str(name) + ": Price: $" + str(item['price']) + ", Quantity: " + str(item['quantity']))

# Initialize inventory with two example items
inventory = {
    "apple": {"price": 0.50, "quantity": 100},
    "banana": {"price": 0.75, "quantity": 150}
}

#Initial inventory.
display_inventory(inventory)

while True:
    print("\n1. Add item\n2. Remove item\n3. Update quantity\n4. Display inventory\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter item name: ")
        price = input("Enter item price: ")
        quantity = int(input("Enter item quantity: "))
        add_item(inventory, name, price, quantity)
        display_inventory(inventory)
    elif choice == "2":
        name = input("Enter item name to remove: ")
        remove_item(inventory, name)
        display_inventory(inventory)
    elif choice == "3":
        name = input("Enter item name to update: ")
        quantity = input("Enter new quantity: ")
        update_quantity(name, quantity)
        display_inventory(inventory)
    elif choice == "4":
        display_inventory(inventory)
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")