import re
from collections import deque
import matplotlib.pyplot as plt

def plot_lagoon(lagoon_matrix, title):
    plt.imshow([[0 if cell == '.' else 1 for cell in row] for row in lagoon_matrix], cmap='gray', interpolation='none')
    plt.title(title)
    plt.show()

def bfs_fill(lagoon_matrix, start, fill_char):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([start])
    lagoon_matrix[start[0]][start[1]] = fill_char

    while queue:
        current_position = queue.popleft()

        for direction in directions:
            new_position = (current_position[0] + direction[0], current_position[1] + direction[1])

            if (
                0 <= new_position[0] < len(lagoon_matrix) and
                0 <= new_position[1] < len(lagoon_matrix[0]) and
                lagoon_matrix[new_position[0]][new_position[1]] == '.'
            ):
                queue.append(new_position)
                lagoon_matrix[new_position[0]][new_position[1]] = fill_char

def calculate_lagoon_capacity(dig_plan):
    lagoon = set()
    current_position = (0, 0)

    for action in dig_plan:
        direction = action[0]
        distance = int(re.search(r'\d+', action).group())

        for _ in range(distance):
            if direction == 'R':
                current_position = (current_position[0] + 1, current_position[1])
            elif direction == 'L':
                current_position = (current_position[0] - 1, current_position[1])
            elif direction == 'U':
                current_position = (current_position[0], current_position[1] - 1)
            elif direction == 'D':
                current_position = (current_position[0], current_position[1] + 1)

            lagoon.add(current_position)

    min_x = min(x for x, _ in lagoon)
    max_x = max(x for x, _ in lagoon)
    min_y = min(y for _, y in lagoon)
    max_y = max(y for _, y in lagoon)

    lagoon_matrix_before = [['.' for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

    for x, y in lagoon:
        lagoon_matrix_before[y - min_y][x - min_x] = '#'

    plot_lagoon(lagoon_matrix_before, "Lagoon Before Flood Fill")

    # hardcoded, beware
    start_position = (1, 70)

    bfs_fill(lagoon_matrix_before, start_position, '#')

    plot_lagoon(lagoon_matrix_before, "Lagoon After Flood Fill")

    total_lava_count = sum(row.count('#') for row in lagoon_matrix_before)

    return total_lava_count

if __name__ == "__main__":
    fin = 'input.txt'
    with open(fin, 'r') as file:
        dig_plan = [line.strip() for line in file]

    result = calculate_lagoon_capacity(dig_plan)
    print("Part 1: The lagoon can contain", result, "cubic meters of lava.")
