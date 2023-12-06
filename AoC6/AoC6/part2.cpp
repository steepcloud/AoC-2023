#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cassert>

void skipNonDigits(std::istringstream& iss) {
    char ch;
    while (iss.get(ch) && !isdigit(ch) && ch != EOF) {
    }
    iss.putback(ch);
}

long long totalWays(int totalTime, long long targetDistance) {
    auto calculateTravelDistance = [totalTime](long long hold) {
        return hold * (totalTime - hold);
    };

    long long low = 0;
    long long high = totalTime / 2;

    if (high * (totalTime - high) < targetDistance) {
        return 0;
    }

    assert(calculateTravelDistance(low) < targetDistance && calculateTravelDistance(high) >= targetDistance);

    while (low + 1 < high) {
        long long mid = (low + high) / 2;
        long long midDistance = calculateTravelDistance(mid);

        if (midDistance >= targetDistance) {
            high = mid;
        }
        else {
            low = mid;
        }
    }

    assert(low + 1 == high);
    assert(calculateTravelDistance(low) < targetDistance && calculateTravelDistance(high) >= targetDistance);

    long long firstValidHold = high;
    assert(calculateTravelDistance(firstValidHold) >= targetDistance && calculateTravelDistance(firstValidHold - 1) < targetDistance);

    long long lastValidHold = (totalTime / 2) + (totalTime / 2 - firstValidHold);

    assert(calculateTravelDistance(lastValidHold) >= targetDistance && calculateTravelDistance(lastValidHold + 2) < targetDistance);

    return lastValidHold - firstValidHold + 2;
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

    std::string timeString, distanceString;
    for (int value : Time) {
        timeString += std::to_string(value);
    }

    for (int value : Distance) {
        distanceString += std::to_string(value);
    }

    int totalTime = std::stoi(timeString) / 10;
    long long targetDistance = std::stoll(distanceString) / 10;

    std::cout << "Time: " << totalTime << std::endl;
    std::cout << "Distance: " << targetDistance << std::endl;

    long long product = 1;

    product = totalWays(totalTime, targetDistance);

    std::cout << "Product: " << product << std::endl;
    return 0;
}
