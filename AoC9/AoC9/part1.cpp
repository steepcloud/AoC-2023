#include <iostream>
#include <fstream>
#include <vector>

int extrapolateForward(std::vector<int>& sequence) {
    long sumFront = sequence[sequence.size() - 1];

    while (sequence.size() >= 2 && sequence.back() != 0) {
        std::vector<int> nextSequence(sequence.size() - 1);
        for (size_t i = 0; i < sequence.size() - 1; ++i) {
            nextSequence[i] = sequence[i + 1] - sequence[i];
        }

        sumFront += nextSequence[nextSequence.size() - 1];

        sequence = std::move(nextSequence);
    }

    return sumFront;
}

int main() {
    std::ifstream fin("input.in");

    std::vector<std::vector<int>> dataset;
    int value;

    while (fin >> value) {
        dataset.emplace_back();
        dataset.back().push_back(value);

        while (fin.peek() != '\n' && !fin.eof()) {
            fin >> value;
            dataset.back().push_back(value);
        }
    }

    fin.close();
    
    int sumForward = 0;
    for (auto& history : dataset) {
        int extrapolatedValue = extrapolateForward(history);
        sumForward += extrapolatedValue;
    }

    std::cout << "Sum of forward extrapolated values: " << sumForward << std::endl;

    return 0;
}
