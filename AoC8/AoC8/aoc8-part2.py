import math
import re

with open("input.in.txt") as file:
    instructions, _, *connection_lines = file.read().split('\n')

connections = {node: destinations for node, *destinations in [re.findall(r'\w+', line) for line in connection_lines]}
nodesA = [node for node in connections if node.endswith('A')]

def stepsZ(start_node, index=0):
    current_node = start_node
    while not current_node.endswith('Z'):
        direction = instructions[index % len(instructions)]
        current_node = connections[current_node][direction == 'R']
        index += 1
    return index

initial_steps = stepsZ('AAA')

lcm_result = math.lcm(*map(lambda start_node: stepsZ(start_node), nodesA))

print('Least common multiple: ', lcm_result)