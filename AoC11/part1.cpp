#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cmath>
#include <algorithm>
// Not working
int main() {
    std::ifstream fin("input.in");
    std::string line;
    std::vector<std::vector<std::string>> galaxy;
    std::vector<int> emptyRows;
    std::vector<int> emptyCols;

    if (!fin.is_open()) {
        std::cerr << "Error opening file." << std::endl;
        return 1;
    }

    while (std::getline(fin, line)) {
        std::vector<std::string> row;

        for (size_t i = 0; i < line.size(); i++) {
            row.push_back(std::string(1, line[i]));
        }

        galaxy.push_back(row);
    }

    for (size_t i = 0; i < galaxy.size(); i++) {
        bool isEmptyRow = true;
        for (size_t j = 0; j < galaxy[i].size(); j++) {
            if (galaxy[i][j] != ".") {
                isEmptyRow = false;
                break;
            }
        }
        if (isEmptyRow) {
            emptyRows.push_back(i);
        }
    }

    for (size_t i = 0; i < galaxy[0].size(); i++) {
        bool isEmptyCol = true;
        for (size_t j = 0; j < galaxy.size(); j++) {
            if (galaxy[j][i] != ".") {
                isEmptyCol = false;
                break;
            }
        }
        if (isEmptyCol) {
            emptyCols.push_back(i);
        }
    }

    auto manhattan = [](std::pair<int, int> p1, std::pair<int, int> p2) {
        auto abs_diff = [](int a, int b) { return a > b ? a - b : b - a; };
        return static_cast<long long>(abs_diff(p1.first, p2.first)) + static_cast<long long>(abs_diff(p1.second, p2.second));
    };

    auto move = [&emptyRows, &emptyCols](std::pair<int, int> g, int q) {
        return std::make_pair(
            g.first + std::count_if(emptyRows.begin(), emptyRows.end(), [g](int r) { return r < g.first; }) * q,
            g.second + std::count_if(emptyCols.begin(), emptyCols.end(), [g](int c) { return c < g.second; }) * q
        );
    };

    long long part1 = 0;
    for (size_t i = 0; i < galaxy.size(); i++) {
        for (size_t j = 0; j < galaxy[i].size(); j++) {
            if (galaxy[i][j] != ".") {
                for (size_t k = i + 1; k < galaxy.size(); k++) {
                    for (size_t l = 0; l < galaxy[k].size(); l++) {
                        if (galaxy[k][l] != ".") {
                            part1 += manhattan(move({ static_cast<int>(i + 1), static_cast<int>(j + 1) }, 2 - 1),
                                move({ static_cast<int>(k), static_cast<int>(l) }, 2 - 1));
                        }
                    }
                }
            }
        }
    }

    long long part2 = 0;
    for (size_t i = 0; i < galaxy.size(); i++) {
        for (size_t j = 0; j < galaxy[i].size(); j++) {
            if (galaxy[i][j] != ".") {
                for (size_t k = i + 1; k < galaxy.size(); k++) {
                    for (size_t l = 0; l < galaxy[k].size(); l++) {
                        if (galaxy[k][l] != ".") {
                            part2 += manhattan(move({ static_cast<int>(i + 1), static_cast<int>(j + 1) }, 1000000 - 1),
                                move({ static_cast<int>(k), static_cast<int>(l) }, 1000000 - 1));
                        }
                    }
                }
            }
        }
    }

    std::cout << "part 1: " << part1 << std::endl;
    std::cout << "part 2: " << part2 << std::endl;

    return 0;
}
