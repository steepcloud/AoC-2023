data_list = list(map(str.split, open('input.txt').read().split('\n\n')))

find_reflection = lambda data, value: next((i for i in range(len(data)) if sum(char1 != char2 for row1, row2 in zip(data[i - 1 :: -1], data[i:]) for char1, char2 in zip(row1, row2)) == value), 0,)

for s_value in 0, 1:
    print(sum(100 * find_reflection(pattern, s_value) + find_reflection([*zip(*pattern)], s_value) for pattern in data_list))
