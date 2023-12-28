import sys
from collections import defaultdict, deque

sys.setrecursionlimit(3_000_000)

read_grid = lambda filename='input.txt': [line.strip() for line in open(filename) if line.strip()]

grid = read_grid()
max_path_length = 0
visited_positions = set()

def dfs(current_position):
    global max_path_length
    if current_position in visited_positions:
        return
    if current_position[0] == len(grid) - 1:
        max_path_length = max(max_path_length, len(visited_positions))
        return

    visited_positions.add(current_position)

    cx, cy = current_position
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nx, ny = cx + dx, cy + dy
        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[nx]) or grid[nx][ny] == "#":
            continue
        if (nx, ny) in visited_positions:
            continue
        dfs((nx, ny))

    visited_positions.remove(current_position)

dfs((0, 1))
print(max_path_length)
