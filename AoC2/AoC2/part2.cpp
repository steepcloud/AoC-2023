#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

struct Cube {
    int count;
    std::string color;
};

struct Game {
    int id, sum_red, sum_green, sum_blue, max_red, max_green, max_blue;
    std::vector<std::vector<Cube>> subsets;
    bool addID;

    // Constructor to initialize members
    Game() : id(0), sum_red(0), sum_green(0), sum_blue(0), addID(false), max_red(0), max_green(0), max_blue(0) {}

    void addCounts(const std::vector<Cube>& subset) {
        for (const Cube& cube : subset) {
            if (cube.color == "red") {
                sum_red += cube.count;
            }
            else if (cube.color == "blue") {
                sum_blue += cube.count;
            }
            else {
                sum_green += cube.count;
            }
        }

        addID = (sum_red <= 12) && (sum_green <= 13) && (sum_blue <= 14);
    }
};

int main() {
    std::ifstream infile("input.in");
    std::string line;
    int sumCubes = 0;

    while (std::getline(infile, line)) {
        std::istringstream iss(line);
        Game game;
        bool flag = true;

        while (!isdigit(iss.peek())) {
            iss.ignore();
        }

        iss >> game.id;

        iss.ignore();

        std::string subset_str;

        while (std::getline(iss, subset_str, ';')) {
            std::istringstream subset_iss(subset_str);
            std::vector<Cube> subset;
            Cube cube;

            while (subset_iss >> cube.count) {
                subset_iss >> std::ws;

                std::getline(subset_iss, cube.color, ',');

                if (!cube.color.empty() && cube.color.back() == ',') {
                    cube.color.pop_back();
                }

                subset.push_back(cube);


            }

            game.addCounts(subset);

            if (game.sum_red > game.max_red) {
                game.max_red = game.sum_red;
            }
            if (game.sum_green > game.max_green) {
                game.max_green = game.sum_green;
            }
            if (game.sum_blue > game.max_blue) {
                game.max_blue = game.sum_blue;
            }

            game.sum_red = 0;
            game.sum_green = 0;
            game.sum_blue = 0;

            game.subsets.push_back(subset);
        }

        if (flag) {
            sumCubes += game.max_red * game.max_green * game.max_blue;
        }
    }

    std::cout << "Sum of valid cubes: " << sumCubes;
    return 0;
}
