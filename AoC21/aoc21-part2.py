def calculateSum(n, a, b, c):
    return a + n * (b - a + (n - 1) * (c - b - b + a) // 2)


def applyModulo(x):
    return complex(x.real % 131, x.imag % 131)


def main():
    grid = {i + j * 1j: cell for i, row in enumerate(open('input.txt'))
            for j, cell in enumerate(row) if cell in '.S'}

    steps_taken = []
    current_positions = {x for x in grid if grid[x] == 'S'}

    for step in range(3 * 131):
        if step % 131 == 65:
            steps_taken.append(len(current_positions))

        current_positions = {p + d for d in {1, -1, 1j, -1j}
                             for p in current_positions if applyModulo(p + d) in grid}

    result = calculateSum(26501365 // 131, *steps_taken)
    print("Part 2:", result)


if __name__ == "__main__":
    main()
