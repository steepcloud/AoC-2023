#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

void skipNonDigits(std::istringstream& iss) {
    char ch;
    while (iss.get(ch) && !isdigit(ch) && ch != EOF) {
    }
    iss.putback(ch);
}

int main() {
    std::ifstream fin("input.in");
    std::string line;

    std::vector<int> Time(5, 0);
    std::vector<int> Distance(5, 0);

    if (fin.is_open()) {
        int index = 0;

        while (std::getline(fin, line)) {
            std::istringstream iss(line);

            std::string token;
            iss >> token;
            if (token == "Time:") {
                skipNonDigits(iss);
                while (iss >> Time[index++] && iss.peek() != EOF);
            }
            else {
                std::istringstream distanceIss(line);
                skipNonDigits(distanceIss);
                int distanceIndex = 0;
                while (distanceIss >> Distance[distanceIndex++] && distanceIss.peek() != EOF);
            }
        }
    }

    fin.close();

    int multiply = 1;
    for (int i = 0; i <= Time.size() - 1; i++) {
        int maxTravelDistance = 0, count = 0;
        for (int hold = 0; hold <= Time[i]; hold++) {
            maxTravelDistance = hold * (Time[i] - hold);

            if (maxTravelDistance > Distance[i]) {
                count++;
            }
        }

        if (count) {
            multiply *= count;
        }
    }

    std::cout << "Product: " << multiply << std::endl;
    return 0;
}
