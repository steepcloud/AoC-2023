import re
from functools import cache

@cache
def arr(remaining_pattern, contig_group, curr_contig = 0):
    s = 0
    if not remaining_pattern:
        return not contig_group and not curr_contig

    if remaining_pattern[0] in ('#', '?'):
        s += arr(remaining_pattern[1:], contig_group, curr_contig + 1)

    if remaining_pattern[0] in ('.', '?') and (contig_group and contig_group[0] == curr_contig or not curr_contig):
        s += arr(remaining_pattern[1:], contig_group[1:] if curr_contig else contig_group)

    return s

F = open("input.txt").read().strip()
Ln = F.split('\n')

S = []
for string in Ln:
    digits = re.findall(r'\d+', string)
    match = re.search(r'^[^ ]+', string)
    pattern = match.group() if match else None
    S.append((pattern, tuple(map(int, digits))))

print('Part 1: ', sum(arr(rp + '.', cog, 0) for rp, cog in S))
print('Part 2: ', sum(arr('?'.join([rp] * 5) + '.', cog * 5) for rp, cog in S))