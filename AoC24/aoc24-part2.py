from collections import defaultdict, deque
from z3 import *

hailstones = []
with open('input.txt', 'r') as file:
    hailstones = list(map(lambda line: (
        tuple(map(int, line.strip().split(' @ ')[0].split(', '))),
        tuple(map(int, line.strip().split(' @ ')[1].split(', ')))
    ), file.readlines()))

rock_position_x = Int('rock_position_x')
rock_position_y = Int('rock_position_y')
rock_position_z = Int('rock_position_z')
rock_velocity_x = Int('rock_velocity_x')
rock_velocity_y = Int('rock_velocity_y')
rock_velocity_z = Int('rock_velocity_z')

formulas = []

for i, hailstone in enumerate(hailstones):
    hailstone_position, hailstone_velocity = hailstone
    time = Int(f'time_{i}')

    formulas.append(rock_position_x + time * rock_velocity_x == hailstone_position[0] + time * hailstone_velocity[0])
    formulas.append(rock_position_y + time * rock_velocity_y == hailstone_position[1] + time * hailstone_velocity[1])
    formulas.append(rock_position_z + time * rock_velocity_z == hailstone_position[2] + time * hailstone_velocity[2])
    formulas.append(time >= 0)
    formulas.append(rock_position_x < 2 ** 128)
    formulas.append(rock_position_y < 2 ** 128)
    formulas.append(rock_position_z < 2 ** 128)

solver = Solver()
solver.add(*formulas)

if solver.check() == sat:
    model = solver.model()
    initial_position_x = model.evaluate(rock_position_x).as_long()
    initial_position_y = model.evaluate(rock_position_y).as_long()
    initial_position_z = model.evaluate(rock_position_z).as_long()

    print(f'Initial Position: ({initial_position_x}, {initial_position_y}, {initial_position_z})')
    print(f'Sum of Coordinates: {initial_position_x + initial_position_y + initial_position_z}')
else:
    print('No solution found.')
