from itertools import combinations

def calculate_manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def move_galaxy(galaxy, empty_rows, empty_cols, q):
    x, y = galaxy
    moved_x = x + sum(row < x for row in empty_rows) * q
    moved_y = y + sum(col < y for col in empty_cols) * q
    return moved_x, moved_y

def main():
    with open("input.txt") as f:
        board = [line.strip() for line in f]

    empty_rows = [index for index, row in enumerate(board) if all(c == '.' for c in row)]
    empty_cols = [i for i in range(len(board[0])) if all(row[i] == '.' for row in board)]
    universe = [(x, y) for x, row in enumerate(board) for y, cell in enumerate(row) if cell != '.']

    manhattan_distance = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    move_galaxy_fn = lambda g, q: (g[0] + sum(r < g[0] for r in empty_rows) * q, g[1] + sum(c < g[1] for c in empty_cols) * q)

    part1 = sum(manhattan_distance(g1, g2) for g1, g2 in combinations([move_galaxy_fn(g, 2 - 1) for g in universe], 2))
    part2 = sum(manhattan_distance(g1, g2) for g1, g2 in combinations([move_galaxy_fn(g, 1000000 - 1) for g in universe], 2))

    print("Part 1:", part1)
    print("Part 2:", part2)

if __name__ == "__main__":
    main()
