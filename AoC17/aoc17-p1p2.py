from heapq import heappop, heappush

def parse_input(filename='input.txt'):
    with open(filename) as file:
        return {(i + j * 1j): int(col) for i, row in enumerate(file) for j, col in enumerate(row.strip())}


def crucible(mini, maxi, end=None, x=0):
    grid = parse_input()
    end = end if end is not None else max(grid.keys(), key=lambda z: (z.real, z.imag))

    dirs = [(0, 0, 0, 1), (0, 0, 0, 1j)]
    visited = set()

    while dirs:
        val, _, pos, direction = heappop(dirs)

        if pos == end:
            return val

        if (pos, direction) in visited:
            continue

        visited.add((pos, direction))

        for turn in [1j / direction, -1j / direction]:
            for step in range(mini, maxi + 1):
                next_pos = pos + turn * step
                if next_pos in grid:
                    step_value = sum(grid[pos + turn * j] for j in range(1, step + 1))
                    heappush(dirs, (val + step_value, x + 1, next_pos, turn))
                    x += 1


print('Part 1:', crucible(1, 3))
print('Part 2:', crucible(4, 10))
