from collections import deque

def navigate_maze():
    # Define symbols
    start_symbol = "S"
    end_symbol = "E"
    path_symbol = "."
    wall_symbol = "#"
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Read maze
    with open("maze-navigator2.txt", "r") as file:
        maze = [list(line.strip()) for line in file.readlines()]

    # Find start and end positions
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == start_symbol:
                start = (i, j)
            if cell == end_symbol:
                end = (i, j)

    # BFS to find path
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)

    # Perform BFS
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            print("Path found:", path)
            return
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and
                maze[nx][ny] != wall_symbol and (nx, ny) not in visited):
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    print("No path found.")

# Run the maze navigator
navigate_maze()