def parse_flow(flow_str):
    flow = {}
    for item in flow_str:
        key, value = item.split("{")
        value = value[:-1].split(",")
        flow[key] = value
    return flow

def evaluate_condition(condition, item):
    if ">" in condition:
        a, b = condition.split(">")
        return item[a] > int(b)
    elif "<" in condition:
        a, b = condition.split("<")
        return item[a] < int(b)

def run_flow(flow, item):
    current_flow = "in"
    while True:
        for condition_action in flow[current_flow]:
            if ":" in condition_action:
                condition, action = condition_action.split(":")
                if evaluate_condition(condition, item):
                    if action == "A":
                        return True
                    elif action == "R":
                        return False
                    else:
                        current_flow = action
                        break
            elif condition_action == "A":
                return True
            elif condition_action == "R":
                return False
            else:
                current_flow = condition_action

def main():
    D = open("input.txt").read().split("\n\n")

    flow_str = D[0].split("\n")
    flows = parse_flow(flow_str)

    items = D[1].split("\n")

    result = 0
    for item_str in items:
        item = {}
        for attribute in item_str[1:-1].split(","):
            key, value = attribute.split("=")
            item[key] = int(value)

        if run_flow(flows, item):
            result += sum(item.values())

    print('Part 1: ', result)

if __name__ == "__main__":
    main()
