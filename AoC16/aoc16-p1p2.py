import sys

sys.setrecursionlimit(1_000_000)

def read_input(filename='input.txt'):
    return [list(line) for line in open(filename).read().strip().split('\n')]

def illuminate(start, illum, grid, mirrors, directions):
    x, y, direction = start
    if (x, y, direction) in illum:
        return
    illum.add((x, y, direction))
    mirror_type = grid[x][y]
    for next_direction in mirrors[mirror_type][direction]:
        next_x, next_y = x + directions[next_direction][0], y + directions[next_direction][1]
        if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
            illuminate((next_x, next_y, next_direction), illum, grid, mirrors, directions)

def count_illuminated_cells(start, grid, mirrors, directions):
    illum = set()
    illuminate(start, illum, grid, mirrors, directions)
    return len(set((x, y) for x, y, _ in illum))

def generate(grid, directions):
    lst = []
    for x in range(len(grid)):
        lst.extend([(x, 0, 'EAST'), (x, len(grid[0]) - 1, 'WEST')])

    for y in range(len(grid[0])):
        lst.extend([(0, y, 'SOUTH'), (len(grid) - 1, y, 'NORTH')])

    return lst

if __name__ == "__main__":
    directions = {'EAST': (0, 1), 'WEST': (0, -1), 'SOUTH': (1, 0), 'NORTH': (-1, 0)}
    grid = read_input()
    mirrors = {
        '.': {'EAST': ['EAST'], 'WEST': ['WEST'], 'SOUTH': ['SOUTH'], 'NORTH': ['NORTH']},
        '-': {'EAST': ['EAST'], 'WEST': ['WEST'], 'SOUTH': ['WEST', 'EAST'], 'NORTH': ['WEST', 'EAST']},
        '|': {'EAST': ['SOUTH', 'NORTH'], 'WEST': ['SOUTH', 'NORTH'], 'SOUTH': ['SOUTH'], 'NORTH': ['NORTH']},
        '/': {'EAST': ['NORTH'], 'WEST': ['SOUTH'], 'SOUTH': ['WEST'], 'NORTH': ['EAST']},
        '\\': {'EAST': ['SOUTH'], 'WEST': ['NORTH'], 'SOUTH': ['EAST'], 'NORTH': ['WEST']},
    }

    start_point = (0, 0, 'EAST')
    l = generate(grid, directions)

    print('Part 1: ', count_illuminated_cells(start_point, grid, mirrors, directions))
    print('Part 2: ', max(count_illuminated_cells(t, grid, mirrors, directions) for t in l))
