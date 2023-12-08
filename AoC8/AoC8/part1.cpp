#include <iostream>
#include <fstream>
#include <unordered_map>
#include <string>

struct Node {
	std::string left, right;
};

int traverseNetwork(const std::unordered_map<std::string, Node>& network, const std::string& start, const std::string& target, const std::string& instructions) {
    std::string currentNode = start;
    int steps = 0;

    while (currentNode != target) {
        Node current = network.at(currentNode);

        if (instructions[steps % instructions.size()] == 'L') {
            currentNode = current.left;
        }
        else if (instructions[steps % instructions.size()] == 'R') {
            currentNode = current.right;
        }
        
        steps++;
    }

    return steps;
}

int main() {
    std::ifstream fin("input.in");
    std::string instructions;
    std::string line;

    std::unordered_map<std::string, Node> network;

    std::string startNode;
    
    if (fin.is_open()) {
        std::getline(fin, instructions);
        
        std::getline(fin, line);

        while (std::getline(fin, line)) {
            size_t equalPos = line.find('=');

            std::string nodeName = line.substr(0, equalPos - 1);

            size_t commaPos = line.find(',');

            Node node;
            node.left = line.substr(equalPos + 3, commaPos - equalPos - 3);
            node.right = line.substr(commaPos + 2, line.size() - commaPos - 3);

            network[nodeName] = node;
        }
    }
    
    fin.close();

    startNode = "AAA";

    std::string targetNode = "ZZZ";

    int steps = traverseNetwork(network, startNode, targetNode, instructions);

    std::cout << "Steps: " << steps << std::endl;

    return 0;
}