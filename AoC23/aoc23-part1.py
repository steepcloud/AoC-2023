from collections import deque

read_grid = lambda filename='input.txt': [line.strip() for line in open(filename) if line.strip()]

initialize_distances = lambda: {((0, 1), (-1, 1)): 0, ((1, 1), (0, 1)): 1}

is_valid_move = lambda grid, x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])

update_distances = lambda distances, current_point, previous_point, current_distance: \
    distances.__setitem__((current_point, previous_point), current_distance) \
    if (current_point, previous_point) not in distances or distances[(current_point, previous_point)] < current_distance else None

def find_longest_hike(grid):
    distances = initialize_distances()
    bfs_queue = deque()
    bfs_queue.append(((1, 1), (0, 1), 1))
    max_distance = 0

    while bfs_queue:
        current_point, previous_point, current_distance = bfs_queue.popleft()

        if distances[(current_point, previous_point)] != current_distance:
            continue

        if current_point[0] == len(grid) - 1:
            max_distance = max(max_distance, current_distance)
            continue

        cx, cy = current_point
        next_steps = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        if grid[cx][cy] == '<': next_steps = [(0, -1)]
        elif grid[cx][cy] == '>': next_steps = [(0, 1)]
        elif grid[cx][cy] == 'v': next_steps = [(1, 0)]
        elif grid[cx][cy] == '^': next_steps = [(-1, 0)]

        for dx, dy in next_steps:
            nx, ny = cx + dx, cy + dy

            if not is_valid_move(grid, nx, ny) or grid[nx][ny] == '#':
                continue

            if (nx, ny) == previous_point or (grid[nx][ny] != '.' and (nx, ny) == (current_point[0] - dx, current_point[1] - dy)):
                continue

            if ((nx, ny), current_point) not in distances or distances[((nx, ny), current_point)] < distances[(current_point, previous_point)] + 1:
                distances[((nx, ny), current_point)] = distances[(current_point, previous_point)] + 1
                bfs_queue.append(((nx, ny), current_point, distances[((nx, ny), current_point)]))

    return max_distance

def main():
    fin = 'input.txt'
    grid = read_grid(fin)
    longest_hike = find_longest_hike(grid)
    print('Part 1:', longest_hike)

if __name__ == "__main__":
    main()
