def apply_mappings(value, mappings):
    for dest, source, length in mappings:
        if source <= value < source + length:
            return dest + (value - source)
    return value

def main():
    with open("input.txt", "r") as file:
        seeds = []
        mappings = {
            "seed-to-soil": [],
            "soil-to-fertilizer": [],
            "fertilizer-to-water": [],
            "water-to-light": [],
            "light-to-temperature": [],
            "temperature-to-humidity": [],
            "humidity-to-location": []
        }

        currMap = None

        for line in file:
            if line.startswith("seeds:"):
                seeds = list(map(int, line.split()[1:]))
            elif "map:" in line:
                currMap = line.split()[0]
                continue
            elif currMap and line.strip():
                mappings[currMap].append(list(map(int, line.split())))

    seed_locations = []

    for seed in seeds:
        soil = apply_mappings(seed, mappings["seed-to-soil"])
        fertilizer = apply_mappings(soil, mappings["soil-to-fertilizer"])
        water = apply_mappings(fertilizer, mappings["fertilizer-to-water"])
        light = apply_mappings(water, mappings["water-to-light"])
        temperature = apply_mappings(light, mappings["light-to-temperature"])
        humidity = apply_mappings(temperature, mappings["temperature-to-humidity"])
        location = apply_mappings(humidity, mappings["humidity-to-location"])

        print(f"Seed {seed} corresponds to location {location}")
        seed_locations.append(location)

    lowest_location = min(seed_locations)

    print("Lowest location number:", lowest_location)

if __name__ == "__main__":
    main()