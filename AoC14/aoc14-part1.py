import re

D = open('input.txt').read().replace('\n', ' ')

rot_90 = lambda r: ' '.join(map(''.join, zip(*(r.split())[:: -1])))
load = lambda l: sum(i for r in l.split() for i, c in enumerate(r[:: -1], 1) if c == 'O')
cycle = lambda c: re.sub('[.O]+', lambda x:''.join(sorted(x[0])[:: -1]), rot_90(c))

print('Part 1: ', load(cycle(rot_90(rot_90(D)))))

