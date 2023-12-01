#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <unordered_map>

int whole_number(const int fdigit, const int ldigit) {
	return fdigit * 10 + ldigit;
}

int main() {
	std::ifstream fin ("input.in");
	int first_digit, last_digit, sum = 0;

	first_digit = last_digit = -1;

	if (fin.is_open()) {
		char chr;
		std::unordered_map<std::string, int> digitMap;
		std::string word;
		std::string currentWord;
		int value = 0;

		std::ifstream fnumber("numbers.txt");

		if (fnumber.is_open()) {
			while (fnumber >> word) {
				digitMap[word] = value++;
			}
		}
		
		fnumber.close();

		while (fin) {
			chr = fin.get();

			if (isalpha(chr)) {
				currentWord += chr;
			}
			else {
				if (!currentWord.empty()) {
					std::string longestMatch;

					for (int i = 0; i < currentWord.size(); ++i) {
						for (int j = 1; j <= currentWord.size() - i; ++j) {
							std::string substr = currentWord.substr(i, j);

							auto it = digitMap.find(substr);
							if (it != digitMap.end()) {
								if (first_digit == -1) {
									first_digit = it->second;
								}
								else {
									last_digit = it->second;
								}

								if (longestMatch.empty() || substr.size() > longestMatch.size()) {
									longestMatch = substr;
								}
								break;
							}
						}
					}
					if (!longestMatch.empty()) {
						currentWord.clear();
					}
				}
			}

			if (isdigit(chr) && first_digit == -1) {
				first_digit = chr - '0';
			} else if (isdigit(chr)) {
				last_digit = chr - '0';
			}

			if (last_digit == -1) {
				last_digit = first_digit;
			}

			if (chr == '\n' || fin.eof()) {
				sum += whole_number(first_digit, last_digit);
				currentWord.clear();
				first_digit = last_digit = -1;
			}
		}

		fin.close();
	}

	std::cout << "Sum of input file: " << sum;
	
	return 0;
}