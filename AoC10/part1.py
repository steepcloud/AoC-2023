from collections import defaultdict, deque

NORTH, SOUTH, EAST, WEST = -1, +1, +1j, -1j

EXITS = {'|': (NORTH, SOUTH), '-': (EAST, WEST),
         'L': (NORTH, EAST), 'J': (NORTH, WEST),
         '7': (SOUTH, WEST), 'F': (SOUTH, EAST),
         '.': (), 'S': (NORTH, EAST, SOUTH, WEST)}

board = {(position := 2 * i + 2j * j): [position + exit_dir for exit_dir in EXITS[cell]]
         for i, row in enumerate(open('input'))
         for j, cell in enumerate(row.strip())}

start = next(key for key, value in board.items() if len(value) == 4)
graph = defaultdict(set)

for position, exits in board.items():
    for exit_position in exits:
        graph[position].add(exit_position)
        graph[exit_position].add(position)

distances = defaultdict(lambda: 1_000_000)

queue = deque([(start, 0)])
while queue:
    current_position, current_distance = queue.popleft()
    distances[current_position] = current_distance
    for adjacent_position in graph[current_position]:
        if distances[adjacent_position] > current_distance:
            queue.append((adjacent_position, current_distance + 1))

max_distance = max(distances.values()) // 2
print(max_distance)