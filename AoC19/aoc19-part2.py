from copy import deepcopy

def parse_flow(flow_str):
    flows = {}
    for item in flow_str:
        key, value = item.split("{")
        value = value[:-1].split(",")
        flows[key] = value
    return flows

def size_of_range(rng):
    result = 1
    for value_range in rng.values():
        result *= value_range[1] - value_range[0] + 1
    return result

def execute_flow(rng, flow):
    result = 0

    for action in flows[flow]:
        if ":" in action:
            condition, next_flow = action.split(":")
            if ">" in condition:
                variable, threshold = condition.split(">")
                new_rng = deepcopy(rng)
                if new_rng[variable][1] > int(threshold):
                    new_rng[variable][0] = max(new_rng[variable][0], int(threshold) + 1)
                    if next_flow == "A":
                        result += size_of_range(new_rng)
                    elif next_flow != "R":
                        result += execute_flow(new_rng, next_flow)
                    rng[variable][1] = min(rng[variable][1], int(threshold))
            elif "<" in condition:
                variable, threshold = condition.split("<")
                new_rng = deepcopy(rng)
                if new_rng[variable][0] < int(threshold):
                    new_rng[variable][1] = min(new_rng[variable][1], int(threshold) - 1)
                    if next_flow == "A":
                        result += size_of_range(new_rng)
                    elif next_flow != "R":
                        result += execute_flow(new_rng, next_flow)
                    rng[variable][0] = max(rng[variable][0], int(threshold))
        else:
            if action == "A":
                result += size_of_range(rng)
            elif action != "R":
                result += execute_flow(rng, action)
    return result

if __name__ == "__main__":
    D = open("input.txt").read().split("\n\n")
    flow_str = D[0].split("\n")
    flows = parse_flow(flow_str)

    initial_range = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
    starting_flow = "in"
    print('Part 2: ', execute_flow(initial_range, starting_flow))
