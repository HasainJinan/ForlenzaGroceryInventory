from time import sleep
import sys
hr = "------------------------------------------"
option_list = ["1. Add item", "2. Remove item", "3. Update quantity", "4. Exit"]

def add_item(inventory, name, price, quantity):
    """
    Add a new item to the inventory.
    
    Args:
    inventory (dict): The current inventory
    name (str): The name of the item
    price (str): The price of the item
    quantity (str): The quantity of the item
    """
    if name.strip().lower() in inventory:
        choose = input("Are you sure you want to overwrite this item? Y/N: ")
        if choose == "Y":
            inventory[name.strip().lower()] = {"price": price, "quantity": quantity}
            print(f"{name.strip().lower()} added to the inventory.")
        elif choose == "N":
            pass
        else:
            print("Sorry I do not understand.")
    else:
        inventory[name.strip().lower()] = {"price": price, "quantity": quantity}
        print(f"{name.strip().lower()} added to the inventory.")

def remove_item(inventory, item_name):
    """
    Remove an item from the inventory.
    
    Args:
    inventory (dict): The current inventory
    item_name (str): The name of the item to remove
    """
    try:
        del inventory[item_name.strip()]
    except:
        print(item_name.strip(), " does not exist in the inventory.")
        x = item_name.lower().strip()
        if x in inventory:
            auto = input(f"Did you mean {x}? Y/N: ")
            if auto == "Y":
                del inventory[x]
                print(x.strip(), " removed from the inventory.")
            else:
                pass
    else:
        print(f"{item_name.strip()} removed from the inventory.")

def update_quantity(inventory, item_name, new_quantity):
    """
    Update the quantity of an item in the inventory.
    
    Args:
    inventory (dict): The current inventory
    item_name (str): The name of the item to update
    new_quantity (str): The new quantity of the item
    """
    try:
        inventory[item_name.strip()]['quantity'] = new_quantity
    except:
        print(item_name.strip(), " does not exist in the inventory.")
        x = item_name.lower().strip()
        if x in inventory:
            auto = input(f"Did you mean {x}? Y/N: ")
            if auto == "Y":
                inventory[x]['quantity'] = new_quantity
                print(f"{x} quantity updated to {new_quantity}.")
            else:
                pass
    else:
        print(f"{item_name.strip()} quantity updated to {new_quantity}.")

def display_inventory(inventory):
    """
    Display all items in the inventory.
    
    Args:
    inventory (dict): The current inventory
    """
    print()
    for char in hr:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.01)
    print()
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        sleep(0.2)
        for name in inventory:
            item = inventory[name]
            print(f"{name}: Price: ${item['price']:.2f}, Quantity: {item['quantity']}")
            sleep(0.2)
    for char in hr:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.01)
    print()
    print()

# Initialize inventory with two example items
inventory = {
    "apple": {"price": 0.50, "quantity": 100},
    "banana": {"price": 0.75, "quantity": 150}
}

#Initial inventory.
display_inventory(inventory)

while True:
    for option in option_list:
        print(option)
        sleep(0.2)
    choice = input("Enter your choice (1-5): ")
    print()
    print()

    if choice == "1":
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
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
        update_quantity(inventory, name, quantity)
        display_inventory(inventory)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")