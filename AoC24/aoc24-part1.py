from collections import defaultdict, deque
from fractions import Fraction

TEST_AREA_START = 200000000000000
TEST_AREA_END = 400000000000000

process_line = lambda line: hailstones.append((tuple(map(int, line.strip().split(' @ ')[0].split(', '))),
                                               tuple(map(int, line.strip().split(' @ ')[1].split(', ')))))

hailstones = []
with open('input.txt', 'r') as file:
    list(map(process_line, file))

slope = lambda v: Fraction(v[1], v[0])
check_condition = lambda v, x, p: (v[0] > 0 and x > p[0]) or (v[0] < 0 and x < p[0])

intersection_count = 0
for i, hailstone1 in enumerate(hailstones):
    for j in range(i + 1, len(hailstones)):
        hailstone2 = hailstones[j]

        position1, velocity1 = hailstone1
        position2, velocity2 = hailstone2

        slope1 = slope(velocity1)
        slope2 = slope(velocity2)

        if slope1 == slope2:
            assert (position1 != position2)
            continue

        intercept1 = position1[1] - slope1 * position1[0]
        intercept2 = position2[1] - slope2 * position2[0]

        x_intersection = (intercept2 - intercept1) / (slope1 - slope2)

        if check_condition(velocity1, x_intersection, position1) and check_condition(velocity2, x_intersection, position2):
            y_intersection = slope1 * x_intersection + intercept1

            if TEST_AREA_START <= x_intersection <= TEST_AREA_END and TEST_AREA_START <= y_intersection <= TEST_AREA_END:
                intersection_count += 1

print('Part 1:', intersection_count)
