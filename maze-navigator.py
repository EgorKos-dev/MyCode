# Import necessary libraries
from collections import deque
# Define function to navigate the maze
def navigate_maze():
    # Define symbols
    start_symbol = "S"
    end_symbol = "E"
    wall_symbol = "#"
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Read maze
    with open("maze-navigator2.txt", "r") as file:
        maze = [list(line.strip()) for line in file.readlines()]

    # Find start and end positions using enumeration
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            # Locate start and end
            if cell == start_symbol:
                start = (i, j)
            if cell == end_symbol:
                end = (i, j)

    # BFS to find path
    queue = deque()
    queue.append((start, [start]))
    # Set to keep track of visited positions
    visited = set()
    visited.add(start)

    # Perform BFS
    while queue:
        (x, y), path = queue.popleft()
        # Check if we've reached the end
        if (x, y) == end:
            print("Path found:", path)
            return
        # Explore neighbors
        for dx, dy in directions:
            # Determine new, potential position
            nx, ny = x + dx, y + dy
            # Check if new position is valid (within bounds, not a wall, not visited)
            if (0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and
                maze[nx][ny] != wall_symbol and (nx, ny) not in visited):
                # Add new position to queue and mark as visited
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    # In case if no path is found
    print("No path found.")

# Run the maze navigator
navigate_maze()