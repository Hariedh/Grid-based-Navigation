import random

def generate_random_grid(size, obstacle_probability):
    grid = [["E" if random.random() > obstacle_probability else "X" for _ in range(size)] for _ in range(size)]
    return grid

def random_walk(grid, start, goal):
    x, y = start
    current = start
    path = [start]

    while current != goal:
        # Generate a random move (up, down, left, right)
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(moves)

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != "X":
                current = (new_x, new_y)
                path.append(current)
                x, y = new_x, new_y
                break
        else:
            # If no valid moves are available, backtrack.
            if len(path) > 1:
                path.pop()
                current = path[-1]
                x, y = current
            else:
                return None  # No path found

    return path

# Example usage:
grid_size = 5
obstacle_probability = 0.3
grid = generate_random_grid(grid_size, obstacle_probability)
start = (0, 0)
goal = (grid_size - 1, grid_size - 1)

print("Random Grid:")
for row in grid:
    print(" ".join(row))
print(f"Start: {start}, Goal: {goal}")

path = random_walk(grid, start, goal)
if path:
    print("Randomly generated path:", path)
else:
    print("No path found")
