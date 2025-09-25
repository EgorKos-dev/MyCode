# Set up a function
def inventory_checker():
    # Initialize variables
    ItemFound = False
    InventoryList = ["Health Potion", "Iron Sword", "Leather Armor", "Map", "Gold Coin"]
    ListLength = len(InventoryList)
    # Prompt user for input and check if the item is in the inventory list
    print("Welcome to your inventory! Enter the item you are looking for:")
    item = input().strip('.,!?;"()[]{}/')
    # Use a for loop and linear search to check if the item is in the inventory list
    for i in range(ListLength):
        if item.lower() == InventoryList[i].lower():
            ItemFound = True
            FoundItem = InventoryList[i]
            # Exit the loop early if the item is found
            break
    # Print the result
    if ItemFound:
        print(f"{FoundItem} found successfully in inventory!")
    # Handle the case where the item is not found
    else:
        print(f"Error: {item} is not in your inventory.")

# Call the function to run the inventory checker
inventory_checker()