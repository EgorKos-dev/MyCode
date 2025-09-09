# Define the main function 
def daisy_counter():
    # Initialize an empty list to use as a stack
    daisy_counter = []
    # Give an option to push the number of daisies found onto the stack
    # Give an option to pop the last value off the stack if incorrect
    # Give an option to peek at the top value of the stack without removing it
    # Give an option to exit the program
    while True:
        action = input("Type 'push' to add daisies, 'pop' to remove the last entry, 'peek' to check the  or 'exit' to quit: ").strip().lower()
        if action == 'push':
            try:
                daisies = int(input("Enter the number of daisies found: "))
                if daisies < 0:
                    print("Error: Number of daisies cannot be negative.")
                    continue
                daisy_counter.append(daisies)
                print(f"Added {daisies} daisies. Current stack: {daisy_counter}")
            except ValueError:
                print("Error: Please enter a valid integer.")
        elif action == 'pop':
            if daisy_counter:
                removed = daisy_counter.pop()
                print(f"Removed {removed} daisies. Current stack: {daisy_counter}")
            else:
                print("The stack is empty. No daisies to remove.")
        elif action == 'peek':
            if daisy_counter:
                print(f"Top value (most recent entry): {daisy_counter[-1]}")
            else:
                print("The stack is empty.")
        elif action == 'exit':
            print("Exiting the Daisy Counter. Goodbye!")
            break
        else:
            print("Invalid action. Please type 'push', 'pop', 'peek', or 'exit'.")
