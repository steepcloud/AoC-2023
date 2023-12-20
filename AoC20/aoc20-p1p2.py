from collections import deque
from math import lcm

class PulsePropagation:
    def __init__(self, input_file):
        self.adjacencies, self.conjunctions, self.flipflops, self.rx_conj = self.parse_input(input_file)
        self.low_pulses = 0
        self.high_pulses = 0
        self.presses = 0
        self.rx_conj_presses = {}

    def parse_input(self, data):
        adjacencies = {}
        conjunctions = {}
        flipflops = {}
        rx_conjunction = ""

        for line in data:
            module, dests = line.split(" -> ")
            dests = dests.split(", ")
            module_type, label = module[0], module[1:]

            if module == "broadcaster":
                adjacencies["broadcaster"] = dests
            else:
                adjacencies[label] = dests

            if "rx" in dests:
                rx_conjunction = label

            if module_type == "&":
                conjunctions[label] = {}

            if module_type == "%":
                flipflops[label] = False

        return adjacencies, conjunctions, flipflops, rx_conjunction

    def process_adjacencies(self):
        for label, dests in self.adjacencies.items():
            for dest in dests:
                if dest in self.conjunctions:
                    self.conjunctions[dest][label] = 0

    def button_presses(self):
        self.presses += 1

        self.low_pulses += 1 + len(self.adjacencies["broadcaster"])
        queue = deque()
        for dest in self.adjacencies["broadcaster"]:
            queue.append((0, "broadcaster", dest))

        while queue:
            pulse, src, label = queue.popleft()

            if label == "rx":
                continue

            signal = 0
            if label in self.conjunctions:
                self.conjunctions[label][src] = pulse
                if any(val == 0 for val in self.conjunctions[label].values()):
                    signal = 1

            if label in self.flipflops:
                if pulse == 1:
                    continue
                self.flipflops[label] = not self.flipflops[label]
                if self.flipflops[label]:
                    signal = 1

            if signal == 1:
                self.high_pulses += len(self.adjacencies[label])
            else:
                self.low_pulses += len(self.adjacencies[label])

            for dest in self.adjacencies[label]:
                queue.append((signal, label, dest))

            for label, val in self.conjunctions[self.rx_conj].items():
                if val == 1 and label not in self.rx_conj_presses:
                    self.rx_conj_presses[label] = self.presses

    def propagate(self):
        self.process_adjacencies()

        for _ in range(1000):
            self.button_presses()

        print('Part 1:', self.low_pulses * self.high_pulses)

        while len(self.rx_conj_presses) < 4:
            self.button_presses()

        print('Part 2:', lcm(*self.rx_conj_presses.values()))

if __name__ == "__main__":
    fin = open('input.txt').read().split('\n')
    propagation = PulsePropagation(fin)
    propagation.propagate()
