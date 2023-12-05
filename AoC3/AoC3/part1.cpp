#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

bool isValid(char ch) {
	return std::isalnum(ch) == 0 && !std::isdigit(ch) && ch != '.';
}

void calcSum(const std::vector<std::string>& engine) {
	int rows = engine.size();
	int cols = engine[0].size();
	int sum = 0;

	for (int i = 0; i < rows; i++) {
		int j = 0, k;
		bool valid = false, flag;
		int number = 0;

		while (j < cols) {
			k = j;
			flag = false;
			while (!i && isdigit(engine[i][k])) {
				valid = (k > 0 && isValid(engine[i][k - 1])) || (k > 0 && isValid(engine[i + 1][k - 1])) || isValid(engine[i + 1][k]) || (k + 1 < cols && isValid(engine[i + 1][k + 1])) || (k + 1 < cols && isValid(engine[i][k + 1]));
				if (valid) {
					flag = true;
				}
				number = number * 10 + int(engine[i][k]) - '0';
				k++;
			}

			if (isdigit(engine[i][k]) && i) {
				while (isdigit(engine[i][k])) {
					valid = (k > 0 && isValid(engine[i - 1][k - 1])) || (k > 0 && isValid(engine[i][k - 1])) || (k > 0 && (i + 1 < rows) && isValid(engine[i + 1][k - 1])) || (i + 1 < rows && isValid(engine[i + 1][k])) || ((k + 1 < cols) && (i + 1 < rows) && isValid(engine[i + 1][k + 1])) || (k + 1 < cols && isValid(engine[i][k + 1])) || (k + 1 < cols && isValid(engine[i - 1][k + 1])) || isValid(engine[i - 1][k]);
					if (valid) {
						flag = true;
					}
					number = number * 10 + int(engine[i][k]) - '0';
					k++;
				}
			}
			
			if (flag) {
				sum += number;
				number = 0;
				valid = !valid;
			}
			else {
				number = 0;
			}

			if (k != j) {
				j = k;
			}
			else {
				j++;
			}
			
		}
	}
	std::cout << "Sum is: " << sum << std::endl;
}

int main() {
	std::ifstream fin("input.in");
	std::vector<std::string> engRows;
	std::string line;

	while (std::getline(fin, line)) {
		engRows.push_back(line);
	}

	calcSum(engRows);

	return 0;
}