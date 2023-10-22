import random
import heapq

def generate_random_grid(size, obstacle_probability):
    grid = [["E" if random.random() > obstacle_probability else "X" for _ in range(size)] for _ in range(size)]
    return grid

def astar_search(grid, start, goal):
    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    def is_valid(cell):
        x, y = cell
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != "X"

    open_list = [(0, start, [])]  # Priority queue (f-value, cell, path)
    closed_set = set()

    while open_list:
        f, current, path = heapq.heappop(open_list)
        if current == goal:
            return path

        if current in closed_set:
            continue

        closed_set.add(current)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = current[0] + dx, current[1] + dy
            neighbor = (x, y)

            if is_valid(neighbor):
                new_path = path + [neighbor]
                g = len(new_path)
                h = heuristic(neighbor)
                f = g + h
                heapq.heappush(open_list, (f, neighbor, new_path))

    return None

# Generate a random grid (change the size and obstacle_probability as needed)
grid_size = 5
obstacle_probability = 0.3
grid = generate_random_grid(grid_size, obstacle_probability)

# Generate random start and goal positions
start = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
goal = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))

print("Random Grid:")
for row in grid:
    print(" ".join(row))
print(f"Start: {start}, Goal: {goal}")

path = astar_search(grid, start, goal)
if path:
    print("Shortest path:", path)
else:
    print("No path found")
