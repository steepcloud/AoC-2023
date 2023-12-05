def apply_mappings(value, mappings):
    for dest, source, length in mappings:
        if source <= value < source + length:
            return dest + (value - source)
    return value

def calculate_location(seed, mappings):
    location = seed
    for mapping_type in mappings:
        location = apply_mappings(location, mappings[mapping_type])
    return location

def main():
    with open("input.txt", "r") as file:
        seeds_ranges = []
        mappings = {
            "seed-to-location": []
        }

        currMap = None

        for line in file:
            if line.startswith("seeds:"):
                seeds_ranges = [list(map(int, line.split()[i:i + 2])) for i in range(1, len(line.split()), 2)]
            elif "map:" in line:
                currMap = line.split()[0]
                mappings[currMap] = []
                continue
            elif currMap and line.strip():
                mappings[currMap].append(list(map(int, line.split())))

    lowest_location = float('inf')

    for seed_range in seeds_ranges:
        start, length = seed_range
        for seed in range(start, start + length):
            location = calculate_location(seed, mappings)
            lowest_location = min(lowest_location, location)

    print("Lowest location number:", lowest_location)

if __name__ == "__main__":
    main()
