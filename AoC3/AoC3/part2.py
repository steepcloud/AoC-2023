import math
import re
# original code belonging to https://github.com/topaz
def read_engine_schematic(file_path):
    with open(file_path, 'r') as file:
        rows = [line.strip() for line in file.readlines()]
    return rows

def extract_gear_ratios(rows):
    gear_ratios = {(row, col): [] for row in range(len(rows)) for col in range(len(rows[0])) if rows[row][col] not in '0123456789.'}

    for r, row in enumerate(rows):
        for number_match in re.finditer(r'\d+', row):
            neighboring_cells = {(r, c) for r in (r - 1, r, r + 1) for c in range(number_match.start()-1, number_match.end()+1)}

            for cell in neighboring_cells & gear_ratios.keys():
                gear_ratios[cell].append(int(number_match.group()))

    return gear_ratios

def main():
    file_path = 'input.in.txt'
    rows = read_engine_schematic(file_path)
    gear_ratios = extract_gear_ratios(rows)

    total_ratios_sum = sum(sum(ratios) for ratios in gear_ratios.values())
    product_of_pairs = sum(math.prod(ratios) for ratios in gear_ratios.values() if len(ratios) == 2)

    print("Sum of all gear ratios:", total_ratios_sum)
    print("Sum of products of pairs:", product_of_pairs)

if __name__ == "__main__":
    main()
