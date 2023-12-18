instructions = [line.split() for line in open('input.txt')]

directions = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1),
              '0': (1, 0), '1': (0, 1), '2': (-1, 0), '3': (0, -1)}

def calculate_lagoon_capacity(instruction_list, current_position=0, total_lava=1):
    for (x_change, y_change), distance in instruction_list:
        current_position += x_change * distance
        total_lava += y_change * distance * current_position + distance / 2
    return int(total_lava)

instruction_list = [(directions[code[7]], int(code[2:7], 16)) for _, _, code in instructions]
result = calculate_lagoon_capacity(instruction_list)

print("The lagoon can hold an impressive", result, "cubic meters of lava.")
