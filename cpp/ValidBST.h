#pragma once
#include "common.h"
#include "BST.h"

bool isValidBST(BST t)
{
	auto curr = t.root;
	std::stack<BST::nodeBST*> s;
	BST::nodeBST* prev = nullptr;
	while (curr != nullptr || !s.empty())
	{
		while (curr != nullptr)
		{
			s.push(curr);
			curr = curr->left;
		}
		curr = s.top();
		s.pop();
		if (prev != nullptr && curr->val <= prev->val)
			return false;
		prev = curr;
		curr = curr->right;
	}
	return true;
}


void TestIsValidBST()
{
	BST t;

	for (int i = 0; i < 10; i++) {
		std::cout << i << "  ";
		t.insert(genRandomInRange());
	}
		

	showInorderIterative(t.root);
	std::cout << "\n" << isValidBST(t);

}