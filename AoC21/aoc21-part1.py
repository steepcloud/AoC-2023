class StepCounter:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_input(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]

    def BFS(self, get, start, steps):
        current_pos = set([start])

        for _ in range(steps):
            next_pos = set()

            dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for i, j in current_pos:
                for di, dj in dirs:
                    next_pos.add((i + di, j + dj))

            next_pos = {(i, j) for i, j in next_pos if get(i, j) == '.'}

            current_pos = next_pos

        return len(current_pos)

    def run(self, steps):
        lines = self.read_input()
        grid = {(i, j): cell for i, line in enumerate(lines) for j, cell in enumerate(line)}
        start_pos = next(pos for pos, cell in grid.items() if cell == 'S')
        grid[start_pos] = '.'
        return self.BFS(lambda i, j: grid.get((i, j)), start_pos, steps)


if __name__ == "__main__":
    fin = 'input.txt'
    steps = 64

    step_counter = StepCounter(fin)
    result = step_counter.run(steps)

    print('Part 1:', result)
