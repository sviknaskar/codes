#pragma once
#include "common.h"
#include "BST.h"
#include <queue>

int getDepth(BST t)
{
	auto curr = t.root;
	std::queue<BST::nodeBST*> nQ;
	nQ.push(curr);
	int depth = 0;
	while (!nQ.empty())
	{
		int len = nQ.size();
		std::vector<int> currLevel;
		for (int i = 0; i < len; i++) {
			auto node = nQ.front();
			nQ.pop();
			currLevel.push_back(node->val);
			if (node->left != nullptr)
				nQ.push(node->left);
			if (node->right != nullptr)
				nQ.push(node->right);
		}

		for (const auto& i : currLevel)
			std::cout << i << "  ";

		std::cout << "\n";
		depth++;
	}
	return depth;
}


void TestBSTDepth()
{
	BST t;

	for (int i = 0; i < 10; i++) {
		int num = genRandomInRange();
		std::cout << num << "  ";
		t.insert(num);
	}
	std::cout << "\n";
	int depth = getDepth(t);
	std::cout << "Depth: " << depth << "\n";
}