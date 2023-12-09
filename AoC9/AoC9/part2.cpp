#include <iostream>
#include <fstream>
#include <vector>

int extrapolateBackward(std::vector<int>& sequence) {
    long sumBackward = sequence[0];

    while (sequence.size() > 1 && sequence.back() != 0) {
        std::vector<int> prevSequence(sequence.size() - 1);
        for (size_t i = 0; i < sequence.size() - 1; ++i) {
            prevSequence[i] = sequence[i] - sequence[i + 1];
        }

        sumBackward += prevSequence[0];

        sequence = std::move(prevSequence);
    }

    return sumBackward;
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

    int sumBackward = 0;
    for (auto& history : dataset) {
        int extrapolatedValue = extrapolateBackward(history);
        sumBackward += extrapolatedValue;
    }
    
    std::cout << "Sum of backward extrapolated values: " << sumBackward << std::endl;

    return 0;
}
