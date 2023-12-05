#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <limits>
#include <numeric>

void findMaxValue(std::istream& inputStream, long long& overallMax) {
    long long maxValue = std::numeric_limits<long long>::min();
    std::string line;

    while (std::getline(inputStream, line)) {
        std::istringstream iss(line);

        if (line.find("map:") != std::string::npos) {
            maxValue = std::numeric_limits<long long>::min();
            continue;
        }

        long long first, second, third;
        if (iss >> first >> second >> third) {
            long long maxFirstTwo = std::max(first, second);

            long long result = maxFirstTwo + third;

            maxValue = std::max(maxValue, result);
        }

        if (line.empty()) {
            break;
        }
    }

    overallMax = std::max(overallMax, maxValue);
}

std::vector<long long> readSeeds(std::ifstream& fin) {
    std::vector<long long> seeds;

    if (!fin.is_open()) {
        std::cerr << "Error opening the file." << std::endl;
        return seeds;
    }

    std::string seedsLine;
    std::getline(fin, seedsLine);

    std::stringstream seedsStream(seedsLine);
    while (!seedsStream.eof() && !isdigit(seedsStream.peek())) {
        seedsStream.ignore();
    }

    long long seedValue;
    while (seedsStream >> seedValue) {
        seeds.push_back(seedValue);
    }

    return seeds;
}

void initialize(std::map<long long, long long>& inputMap, const long long& size) {
    for (int i = 0; i < size; i++) {
        inputMap[i] = i;
    }
}

void transform(std::map<long long, long long>& inputMap, const long long& dest, const long long& source, const long long& range) {
    for (int i = 0; i < range; i++) {
        long long index = source + i;
        inputMap[index] = dest + i;
    }
}

template <typename K, typename V>
K findMinKey(const std::map<K, V>& inputMap) {
    if (inputMap.empty()) {
        std::cerr << "Error: Input map is empty." << std::endl;
        return std::numeric_limits<K>::max();
    }

    auto minKeyIterator = std::min_element(inputMap.begin(), inputMap.end(), [](const auto& lhs, const auto& rhs) {
            return lhs.first < rhs.first;
        }
    );

    return minKeyIterator->first;
}

int main() {
    std::ifstream fin("input.in");
    std::string line;

    std::vector<long long> seeds = readSeeds(fin);

    std::map<long long, long long> seedToSoilMap;
    std::map<long long, long long> soilToFertilizerMap;
    std::map<long long, long long> fertilizerToWaterMap;
    std::map<long long, long long> waterToLightMap;
    std::map<long long, long long> lightToTemperatureMap;
    std::map<long long, long long> temperatureToHumidityMap;
    std::map<long long, long long> humidityToLocationMap;

    long long overallMax = std::numeric_limits<long long>::min();

    while (!fin.eof()) {
        findMaxValue(fin, overallMax);
    }

    std::cout << "Max value: " << overallMax << std::endl;

    fin.clear();
    fin.seekg(0, std::ios::beg);

    initialize(seedToSoilMap, overallMax);
    initialize(soilToFertilizerMap, overallMax);
    initialize(fertilizerToWaterMap, overallMax);
    initialize(waterToLightMap, overallMax);
    initialize(lightToTemperatureMap, overallMax);
    initialize(temperatureToHumidityMap, overallMax);
    initialize(humidityToLocationMap, overallMax);

    if (seeds.empty()) {
        std::cerr << "Error reading seed values from the file." << std::endl;
        return 1;
    }

    int mapCount = 0;
    bool process = false;

    while (std::getline(fin, line)) {
        size_t mapPos = line.find("map:");

        if (mapPos != std::string::npos) {
            process = true;
            mapCount++;
            continue;
        }

        if (process) {
            std::istringstream iss(line);

            long long dest_val, source_val, range_val;
            if (iss >> dest_val >> source_val >> range_val) {
                switch (mapCount) {
                case 1:
                    transform(seedToSoilMap, dest_val, source_val, range_val);
                    break;
                case 2:
                    transform(soilToFertilizerMap, dest_val, source_val, range_val);
                    break;
                case 3:
                    transform(fertilizerToWaterMap, dest_val, source_val, range_val);
                    break;
                case 4:
                    transform(waterToLightMap, dest_val, source_val, range_val);
                    break;
                case 5:
                    transform(lightToTemperatureMap, dest_val, source_val, range_val);
                    break;
                case 6:
                    transform(temperatureToHumidityMap, dest_val, source_val, range_val);
                    break;
                case 7:
                    transform(humidityToLocationMap, dest_val, source_val, range_val);
                    break;
                default:
                    break;
                }
            }
        }
    }
    
    fin.close();

    long long overallMinKey = std::min({
        findMinKey(seedToSoilMap),
        findMinKey(soilToFertilizerMap),
        findMinKey(fertilizerToWaterMap),
        findMinKey(waterToLightMap),
        findMinKey(lightToTemperatureMap),
        findMinKey(temperatureToHumidityMap),
        findMinKey(humidityToLocationMap)
        });

    std::cout << "Min location: " << overallMinKey << std::endl;

    return 0;
}