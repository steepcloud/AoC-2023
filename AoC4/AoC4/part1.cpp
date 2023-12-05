#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>

void skipNonDigits(std::istringstream& iss) {
	while (!isdigit(iss.peek())) {
		iss.ignore();
	}
}

int main() {
	std::ifstream fin("input.in");
	std::string line;
	int sumPoints = 0;

	if (fin.is_open()) {
		int card, cardPoints = 0, pos, count;
		std::vector<int> winNumbers(11, 0);
		std::vector<int> checkNumbers;

		while (std::getline(fin, line)) {
			std::istringstream iss(line);
			std::istringstream iss2(line);

			skipNonDigits(iss);

			iss >> card;

			iss.ignore();

			pos = 0;
			while (iss >> winNumbers[pos++] && iss.peek() != '|');
			
			while (iss2.peek() != '|')
				iss2.ignore();
			
			if (iss2.peek() == '|') {
				iss2.ignore();
			}
			
			int num;
			while (iss2 >> num) {
				checkNumbers.push_back(num);
			}
			
			count = 0;
			for (int i = 0; i < winNumbers.size() - 1; i++) {
				for (int j = 0; j < checkNumbers.size(); j++) {
					if (winNumbers[i] == checkNumbers[j]) {
						count++;
					}
				}
			}
			if (!count) {
				count = 0;
			}
			else {
				sumPoints += pow(2, count - 1);
			}

			checkNumbers.clear();
		}
	}

	fin.close();

	std::cout << "Total points: " << sumPoints;
	return 0;
}