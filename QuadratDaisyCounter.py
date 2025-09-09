# Define the main function 
def daisy_counter():
    # Initialize an empty list to use as a stack
    daisy_counter = []
    stack_limit = 12
    counter_sum = 0
    # Give an option to push the number of daisies found onto the stack
    # Give an option to pop the last value off the stack if incorrect
    # Give an option to peek at the top value of the stack without removing it
    # Give an option to exit the program
    while True:
        action = input("'push' to add daisies\n 'pop' to remove the last entry\n'peek' to check the last input\n 'LIFO' to perform LIFO (last in, first out) principle\n 'exit' to quit: ").strip().lower()
        # Handle user input for stack operations
        if action == 'push':
            # Add exception handling for non-integer inputs
            try:
                daisies = int(input("Enter the number of daisies found: "))
                if daisies < 0:
                    # Give an error message for negative inputs
                    print("Error: Number of daisies cannot be negative.")
                    continue
                # Add daisies to the stack if within limit
                daisy_counter.append(daisies)
                stack_limit -= 1
                counter_sum += daisies
                print(f"Added {daisies} daisies. Current stack: {daisy_counter}")
            except ValueError:
                print("Error: Please enter a valid integer.")
        # Handle pop, peek, and exit actions
        elif action == 'pop':
            if daisy_counter:
                # Use pop() to remove the last entry from the stack
                removed = daisy_counter.pop()
                print(f"Removed {removed} daisies. Current stack: {daisy_counter}")
                stack_limit += 1
            else:
                # Show an error message if the stack is empty
                print("The stack is empty. No daisies to remove.")
        elif action == 'peek':
            if daisy_counter:
                # Use indexing to view the top value without removing it
                print(f"Top value (most recent entry): {daisy_counter[-1]}")
            else:
                # Show an error message if the stack is empty
                print("The stack is empty.")
        elif action == 'exit':
            # Add an option to exit the program
            print("Exiting the Daisy Counter. Goodbye!")
            break
        # Add an option to perform LIFO (last in, first out) principle and display all counts in the stack by repeatedly popping until empty
        elif action == 'lifo':
            if daisy_counter:
                print("Performing LIFO (last in, first out):")
                while daisy_counter:
                    print("Current stack:", daisy_counter)
                    print("Sum of daisies", counter_sum)
                    print(daisy_counter.pop())
                    counter_sum -= daisy_counter[-1]
                print("All daisies have been removed from the stack.")
                stack_limit = 12
            else:
                print("The stack is empty. No daisies to display.")
        # Show an error message if the stack limit is reached
        elif stack_limit == len(daisy_counter):
            print("Stack limit reached. Cannot add more daisies.")
        else:
            print("Invalid action. Please type 'push', 'pop', 'peek', or 'exit'.")

daisy_counter()