
## REQUIRED LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Maze generating Function
def generate_maze(rows, columns):

    # Creating a grid 
    maze = np.ones((rows, columns))
    
    # Start point as at top-left corner
    start_r, start_c = 0, 0
    
    # Constraint point = 1, Trasversal point = 0
    maze[start_r, start_c] = 0
  
    stack = [(start_r, start_c)]        # Memory of path
    
    # Direction vectors: Right, Left, Down, Up 
    directions = np.array([(0, 2), (0, -2), (2, 0), (-2, 0)])
    
    while stack:
        r, c = stack[-1]  # Current cell
        
        # Calculate all potential neighbor nodes
        current_pos = np.array([r, c])
        neighbor_positions = current_pos + directions
        
        # Filter valid unvisited nodes
        valid_neighbors = []
        for nr, nc in neighbor_positions:
            if 0 <= nr < rows and 0 <= nc < columns and maze[nr, nc] == 1:
                valid_neighbors.append((nr, nc))
        
        if valid_neighbors:
            # Picking a random unvisited neighbor node
            idx = np.random.randint(len(valid_neighbors))
            nr, nc = valid_neighbors[idx]
            
          
            wall_r = (r + nr) // 2
            wall_c = (c + nc) // 2
            maze[wall_r, wall_c] = 0
            
            # Mark node as path
            maze[nr, nc] = 0
            
            # Trasverse to node
            stack.append((nr, nc))
        else:
            # if dead end: backtracking
            stack.pop()
    
    return maze

# Maze solving using DFS algorithm
def solve_maze(maze, start=(0, 0), goal=None):
    rows, columns = maze.shape
    
    # Default goal: bottom-right corner
    if goal is None:
        goal = (rows - 1, columns - 1)
    
    # Stack stores: (current_position, path_to_current)
    stack = [(start, [start])]
    visited = np.zeros((rows, columns), dtype=bool)
  
    directions = np.array([(0, 1), (1, 0), (0, -1), (-1, 0)])
    
    while stack:
        (r, c), path = stack.pop()

        if (r, c) == goal:
            return np.array(path)
        
        # if already visited we skip
        if visited[r, c]:
            continue
        visited[r, c] = True
        
       # nodes in the neighbourhood
        current_pos = np.array([r, c])
        neighbor_positions = current_pos + directions
        
        # Explore neighbors
        for nr, nc in neighbor_positions:
            # Check if neighbor is valid and walkable
            if (0 <= nr < rows and 0 <= nc < columns and 
                maze[nr, nc] == 0 and not visited[nr, nc]):
                # Add neighbor to stack with updated path
                stack.append(((nr, nc), path + [(nr, nc)]))
    
    # if No path found
    return None
