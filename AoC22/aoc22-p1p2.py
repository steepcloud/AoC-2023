from itertools import zip_longest


class SandSlabs:
    def __init__(self, file_path):
        self.input_data = self.process_input(file_path)

    @staticmethod
    def irange(start, stop):
        return range(start, stop + 1) if start <= stop else range(start, stop - 1, -1)

    @staticmethod
    def draw(a, b):
        i1, j1, k1 = a
        i2, j2, k2 = b
        result = zip_longest(SandSlabs.irange(i1, i2), SandSlabs.irange(j1, j2), SandSlabs.irange(k1, k2))
        return set((a or i1, b or j1, c or k1) for a, b, c in result)

    @staticmethod
    def fall(tiles, brick):
        while True:
            down = {(x, y, z - 1) for x, y, z in brick}
            if any(z == 0 for _, _, z in down) or down & tiles:
                return brick
            brick = down

    @staticmethod
    def process_input(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]

    def countSafelyDisintegrableBricks(self):
        tiles = set()
        bricks = []

        for line in self.input_data:
            a, b = [[int(x) for x in r.split(',')] for r in line.split('~')]
            brick = self.draw(a, b)
            bricks.append(brick)
            tiles |= brick

        bricks.sort(key=lambda p: min(z for _, _, z in p))

        for i, brick in enumerate(bricks):
            tiles -= brick
            bricks[i] = self.fall(tiles, brick)
            tiles |= bricks[i]

        res = 0

        for brick in bricks:
            without = tiles - brick
            for other in bricks:
                if other == brick:
                    continue
                without -= other
                if self.fall(without, other) != other:
                    break
                without |= other
            else:
                res += 1

        return res

    def countSafelyDisintegrableBricksWithSupport(self):
        tiles = set()
        bricks = []

        for line in self.input_data:
            a, b = [[int(x) for x in r.split(",")] for r in line.split('~')]
            brick = self.draw(a, b)
            bricks.append(brick)
            tiles |= brick

        bricks.sort(key=lambda p: min(z for _, _, z in p))

        for i, brick in enumerate(bricks):
            tiles -= brick
            bricks[i] = self.fall(tiles, brick)
            tiles |= bricks[i]

        res = 0

        for brick in bricks:
            without = tiles - brick
            for other in bricks:
                if other == brick:
                    continue
                without -= other
                if self.fall(without, other) != other:
                    res += 1
                else:
                    without |= other

        return res


if __name__ == "__main__":
    sand_slabs = SandSlabs('input.txt')

    result_p1 = sand_slabs.countSafelyDisintegrableBricks()
    print('Part 1:', result_p1)

    result_p2 = sand_slabs.countSafelyDisintegrableBricksWithSupport()
    print('Part 2:', result_p2)
