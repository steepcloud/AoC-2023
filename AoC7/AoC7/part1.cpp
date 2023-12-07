#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <unordered_map>

int highestMatching(const std::string& str) {
	if (str.empty()) {
		return 0;
	}

	std::unordered_map<char, int> charCount;

	for (char ch : str) {
		charCount[ch]++;
	}

	int maxCount = 1;
	for (const auto& pair : charCount) {
		if (pair.second > maxCount) {
			maxCount = pair.second;
		}
	}

	if (maxCount == str.size()) {
		return str.size();
	}
	else if (maxCount == 3 && charCount.size() == 2) {
		return 0; // full house
	}
	else if (maxCount == charCount.size()) {
		return maxCount; // 3 of a kind
	}
	else if (maxCount == 2 && charCount.size() == 3) {
		return maxCount; // two pair
	}
	else if (maxCount == 2 && maxCount < charCount.size()) {
		return maxCount - 1; // one pair
	}
	else if (maxCount == 1 && charCount.size() == str.size()){
		return -1; // high card
	}
}

int countLabelOccurrences(const std::string& str, char label) {
	return std::count(str.begin(), str.end(), label);
}

bool isFourOfAKind(const std::string& str) {
	for (char ch : str) {
		if (countLabelOccurrences(str, ch) == 4) {
			return true;
		}
	}
	return false;
}

bool isHighCard(const std::string& str) {
	int maxCount = highestMatching(str);
	return (maxCount == 1) ? -1 : maxCount == 1;
}

int getHandType(const std::string& hand) {
	//std::cout << "Hand: " << hand << std::endl;
	if (highestMatching(hand) == hand.size()) {
		//std::cout << "Five of a kind" << std::endl;
		return 9;
	}
	else if (isFourOfAKind(hand)) {
		//std::cout << "Four of a kind" << std::endl;
		return 8;
	}
	else if (!highestMatching(hand)) {
		//std::cout << "Full house" << std::endl;
		return 7;
	}
	else if (highestMatching(hand) == 3) {
		//std::cout << "Three of a kind" << std::endl;
		return 6;
	}
	else if (highestMatching(hand) == 2) {
		//std::cout << "Two pair" << std::endl;
		return 5;
	}
	else if (highestMatching(hand) == 1) {
		//std::cout << "One pair" << std::endl;
		return 4;
	}
	else if (highestMatching(hand) == -1) {
		//std::cout << "High card" << std::endl;
		return 3;
	}
	else {
		//std::cout << "Unknown hand type" << std::endl;
		return 2;
	}

	//std::cout << std::endl;
}

std::vector<std::string> cards = { "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A" };

int cardStrength(const std::string& card) {
	auto it = std::find(cards.begin(), cards.end(), card);
	if (it != cards.end()) {
		return it - cards.begin();
	}
	return -1;
}

bool customCompare(const std::pair<std::string, int>& a, const std::pair<std::string, int>& b) {
	if (a.second != b.second) {
		return a.second > b.second;
	}
	else {
		const std::string& cardA = a.first;
		const std::string& cardB = b.first;

		for (int i = 0; i < cardA.size() && i < cardB.size(); ++i) {
			int strengthA = cardStrength(std::string(1, cardA[i]));
			int strengthB = cardStrength(std::string(1, cardB[i]));

			if (strengthA != strengthB) {
				return strengthA > strengthB;
			}
		}

		return cardA.size() < cardB.size();
	}
}

int main() {
	std::ifstream fin("input.in");
	std::string line;
	std::vector<int> bid(1000, 0);
	std::vector<std::string> poker(1000);
	
	std::vector<std::pair<std::string, int>> handRanks;
	std::vector<std::pair<std::pair<std::string, int>, int>> indexedHands; // hand, type, init_index

	std::vector<std::string> cardsMain = { "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A" };

	if (fin.is_open()) {
		int index = 0;

		while (std::getline(fin, line)) {
			std::istringstream iss(line);

			while (iss >> poker[index] >> bid[index] && iss.peek() != EOF);
			
			handRanks.push_back({ poker[index], getHandType(poker[index]) });
			indexedHands.push_back({ { poker[index], getHandType(poker[index]) }, index });

			index++;
		}
	}

	fin.close();

	// sorting hands based on type and card values
	std::sort(handRanks.begin(), handRanks.end(), customCompare);

	/*
	std::cout << "indexedHands:" << std::endl;
	for (const auto& pair : indexedHands) {
		std::cout << "Hand: " << pair.first.first << " - Type: " << pair.first.second << " - Original Index: " << pair.second << std::endl;
	}
	*/
	int rank = handRanks.size(),
		totalWinnings = 0;

	for (const auto& pair : handRanks) {
		auto it = std::find_if(indexedHands.begin(), indexedHands.end(), [&pair](const std::pair<std::pair<std::string, int>, int>& indexedPair) {
				return indexedPair.first == pair;
		});

		if (it != indexedHands.end()) {
			int originalIndex = it->second,
				score = rank * bid[originalIndex];

			totalWinnings += score;
			std::cout << "Hand: " << pair.first << " - Type: " << pair.second << " - Rank: " << rank << std::endl;
			rank--;
		}
	}
	
	std::cout << "\nTotal winnings: " << totalWinnings << std::endl;
	return 0;
}