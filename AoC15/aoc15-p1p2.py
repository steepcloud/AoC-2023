from functools import reduce

D = [s.strip() for s in open('input.txt').read().split(',')]

code = lambda s, c: (s + ord(c)) * 17 % 256
hash = lambda s: reduce(code, s, 0)

print('Part 1: ', sum(map(hash, D)))

#ans = 0
#for string in D:
#    current_value = 0
#    for char in string:
#        current_value = (((ord(char) + current_value) * 17)) % 256

#    ans += current_value

#print(ans)

box = [dict() for _ in range(256)]

for s in D:
    match s.strip('-').split('='):
        case [l, f]:
            box[hash(l)][l] = int(f)
        case [l]:
            box[hash(l)].pop(l, 0)

print('Part 2: ', sum(i * j * f for i, b in enumerate(box, 1) for j, f in enumerate(b.values(), 1)))