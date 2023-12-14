import re

D = open('input.txt').read().strip()
L = D.split('\n')
grid = [[c for c in row] for row in L]

def rotate(grid):
    row = len(grid)
    col = len(grid[0])

    new_grid = [['?' for _ in range(row)] for _ in range(col)]

    for r in range(row):
        for c in range(col):
            new_grid[c][row - 1 - r] = grid[r][c]

    return new_grid

def roll(grid):
    row = len(grid)
    col = len(grid[0])

    for c in range(col):
        for _ in range(row):
            for r in range(row):
                if grid[r][c] == 'O' and r > 0 and grid[r - 1][c] == '.':
                    grid[r][c] = '.'
                    grid[r - 1][c] = 'O'

    return grid

score = lambda G: sum((len(G) - r) if c == 'O' else 0 for r, row in enumerate(G) for c in row)
cache = {}

tar = 1_000_000_000
k = 0

while k < tar:
    k += 1

    for j in range(4):
        grid = roll(grid)
        grid = rotate(grid)

    grid_height = tuple(tuple(row) for row in grid)

    if grid_height in cache:
        cycle_length = k - cache[grid_height]
        times = (tar - k) // cycle_length
        k += times * cycle_length

    cache[grid_height] = k
    
print('Part 2: ', score(grid))