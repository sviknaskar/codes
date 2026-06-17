#pragma once
#include "common.h"
#include "BST.h"
#include <queue>

std::vector<std::vector<int>> getLevelOrder(BST t)
{
	auto root = t.root;
	std::queue<BST::nodeBST*> nodeQueue;
	std::vector<std::vector<int>> res;
	nodeQueue.push(root);
	while (!nodeQueue.empty())
	{
		std::vector<int> currLevel;
		int len = nodeQueue.size();

		for (int i = 0; i < len; i++)
		{
			auto node = nodeQueue.front();
			currLevel.push_back(node->val);
			nodeQueue.pop();
			if (node->left != nullptr)
				nodeQueue.push(node->left);
			if (node->right != nullptr)
				nodeQueue.push(node->right);
		}
		res.push_back(currLevel);
	}
	return res;
}

void TestLevelOrderTrav()
{
	BST t;

	for (int i = 0; i < 10; i++) {
		int num = genRandomInRange();
		std::cout << num << "  ";
		t.insert(num);
	}
		


	auto lot = getLevelOrder(t);

	std::cout << "\n";

	for (const auto& i : lot) {
		for (const auto& j : i)
			std::cout << j << "  ";
		std::cout << "\n";
	}

	showInorderIterative(t.root);
}