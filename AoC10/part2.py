import sys
sys.setrecursionlimit(100000000)

with open("input", "r") as f:
    lines = f.readlines()

pipe_types = {
    "|": ["n", "s"],
    "-": ["w", "e"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
    'S': ["n", "s", "w", "e"],
}

directions = {
    "n": (-1, 0, "s"),
    "s": (1, 0, "n"),
    "w": (0, -1, "e"),
    "e": (0, 1, "w"),
}

game_map = [[c for c in line.strip()] for line in lines]

start = next((i, j) for i, row in enumerate(game_map) for j, cell in enumerate(row) if cell == 'S')

encountered_places = {}

def explore(start, distance):
    i, j = start
    if start in encountered_places:
        return
    encountered_places[start] = distance

    for direction in pipe_types[game_map[i][j]]:
        di, dj, opposite = directions[direction]
        new = (i + di, j + dj)

        if 0 <= new[0] < len(game_map) and 0 <= new[1] < len(game_map[new[0]]) and game_map[new[0]][new[1]] in pipe_types:
            target_directions = pipe_types[game_map[new[0]][new[1]]]
            if opposite in target_directions:
                explore(new, distance + 1)

explore(start, 0)

def get_piece_type(i, j):
    reachable_directions = [
        direction for direction in directions
        if 0 <= i + directions[direction][0] < len(game_map) and 0 <= j + directions[direction][1] < len(game_map[i + directions[direction][0]])
        and (i + directions[direction][0], j + directions[direction][1]) in encountered_places
        and game_map[i + directions[direction][0]][j + directions[direction][1]] in pipe_types
        and directions[direction][2] in pipe_types[game_map[i + directions[direction][0]][j + directions[direction][1]]]
    ]

    for piece_type in pipe_types:
        if len(reachable_directions) == len(pipe_types[piece_type]) and all(direction in pipe_types[piece_type] for direction in reachable_directions):
            return piece_type

    return None

game_map[start[0]][start[1]] = get_piece_type(start[0], start[1])

for i, row in enumerate(game_map):
    norths = 0
    for j, cell in enumerate(row):
        if (i, j) in encountered_places:
            pipe_directions = pipe_types[cell]
            norths += pipe_directions.count("n")
            continue

        game_map[i][j] = "O" if norths % 2 == 0 else "I"

inside_count = sum(row.count("I") for row in game_map)
print(inside_count)