#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

struct Cube {
    int count;
    std::string color;
};

struct Game {
    int id, sum_red, sum_green, sum_blue;
    std::vector<std::vector<Cube>> subsets;
    bool addID;

    Game() : id(0), sum_red(0), sum_green(0), sum_blue(0), addID(false) {}

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
    int sumID = 0;

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
            
            /*
            for (const Cube& c : subset) {
                std::cout << c.count << ' ' << c.color << ' ';
            }
            std::cout << std::endl;
            */

            game.addCounts(subset);

            game.sum_red = 0;
            game.sum_green = 0;
            game.sum_blue = 0;

            if (!game.addID) {
                flag = false;
            }

            game.subsets.push_back(subset);
        }

        if (flag) {
            sumID += game.id;
        }
    }

    std::cout << "Sum of valid Game IDs: " << sumID;
    return 0;
}
