# Define a function to allow the user to enqueue planes to land at the airport
def plane_queue():
    # Initialize an empty list to use as a queue
    plane_queue = []
    # Give an option to enqueue a plane to the queue
    # Give an option to to front to view the next plane to land without removing it
    # Give an option to dequeue a plane from the queue if it has landed
    # Give an option to perform FIFO (first in, first out) principle and simulate planes landing, showing the order they land in
    # Give an option to exit the program
    while True:
        action = input("'enqueue' to add a plane\n 'dequeue' to remove the next plane\n'front' to check the next plane\n 'FIFO' to perform FIFO (first in, first out) principle\n 'exit' to quit: ").strip().lower()
        # Handle user input for queue operations
        if action == 'enqueue':
            plane = input("Enter the flight number of the plane to enqueue: ").strip().upper()
            # Add the plane to the end of the queue
            plane_queue.append(plane)
            print(f"Enqueued plane {plane}. Current queue: {plane_queue}")
        elif action == 'dequeue':
            if plane_queue:
                # Use pop(0) to remove the first entry from the queue
                landed_plane = plane_queue.pop(0)
                print(f"Plane {landed_plane} has landed and been removed from the queue. Current queue: {plane_queue}")
            else:
                # Show an error message if the queue is empty
                print("The queue is empty. No planes to dequeue.")
        elif action == 'front':
            if plane_queue:
                # Use indexing to view the front value without removing it
                print(f"Next plane to land: {plane_queue[0]}")
            else:
                # Show an error message if the queue is empty
                print("The queue is empty.")
        elif action == 'exit':
            # Add an option to exit the program
            print("Exiting the Airport Queue system. Goodbye!")
            break
        # Add an option to perform FIFO (first in, first out) principle and display all planes in the queue by repeatedly dequeuing until empty
        elif action == 'fifo':
            if plane_queue:
                print("Performing FIFO (first in, first out):")
                while plane_queue:
                    print("Current queue:", plane_queue)
                    # Dequeue the first entry and display it
                    landed_plane = plane_queue.pop(0)
                    print(f"Plane {landed_plane} has landed and been removed from the queue.")
                # After all planes have landed, show that the queue is empty
                print("All planes have landed and the queue is now empty.")
            else:
                print("The queue is empty. No planes to land.")
        else:
            # Handle invalid actions
            print("Invalid action. Please type 'enqueue', 'dequeue', 'front', 'FIFO', or 'exit'.")
# Call the main function to start the program
plane_queue()