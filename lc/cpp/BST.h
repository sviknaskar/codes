#pragma once
#include "common.h"


struct BST {

	BST() :root(nullptr) {}
	void insert(int v) {
		auto tmpNode = new nodeBST(v);

		if (root == nullptr)
		{
			root = tmpNode;
			return;
		}
		auto curr = root;
		while (true) {
			if (curr->val >= v)
			{
				if (curr->left == nullptr)
				{
					curr->left = tmpNode;
					break;
				}
				else
					curr = curr->left;
			}
			else {
				if (curr->right == nullptr)
				{
					curr->right = tmpNode;
					break;
				}
				else
					curr = curr->right;
			}
		}
	}

	struct nodeBST {
		int val;
		nodeBST* left;
		nodeBST* right;
		nodeBST(int v) :val(v), left(nullptr), right(nullptr) {}
	};
	nodeBST* root;
};

using nodeBst = BST::nodeBST;


void showInorder(BST::nodeBST* root) {
	if (root == nullptr)
		return;
	auto curr = root;
	showInorder(curr->left);
	std::cout << curr->val << "  ";
	showInorder(curr->right);
}


void showPreorder(BST::nodeBST* root) {
	if (root == nullptr)
		return;
	auto curr = root;
	std::cout << curr->val << "  ";
	showInorder(curr->left);
	showInorder(curr->right);
}


void showInorderIterative(BST::nodeBST* root) {
	std::stack<BST::nodeBST*> s;
	auto curr = root;
	while (curr != nullptr || !s.empty()) {
		while (curr != nullptr)
		{
			s.push(curr);
			curr = curr->left;
		}
		curr = s.top();
		s.pop();
		std::cout << curr->val << " ";
		curr = curr->right;
	}
	std::cout << "\n";
}


 void convertBstToIncreasingOrder(nodeBst* root, nodeBst& res)
{
	using node = nodeBst;

	if (root == nullptr)
		return;
	
	std::stack<node*> s;
	node* prev = &res;
	node* curr = root;
	while (curr != nullptr || !s.empty())
	{
		while (curr != nullptr)
		{
			s.push(curr);
			curr = curr->left;
		}
		curr = s.top();
		s.pop();
		curr->left = nullptr;
		prev->right = curr;
		prev = prev->right;

		curr = curr->right;
	}
	std::cout << "pause\n";
}


void showLevelOrder(nodeBst* root)
{
	if (root == nullptr)
		return;
	//level order trav
	std::queue<nodeBst*> q;
	q.push(root);
	while (!q.empty())
	{
		int len = q.size();
		std::vector<int> levelVals;
		for (int i = 0; i < len; i++)
		{
			auto curr = q.front();
			levelVals.push_back(curr->val);
			q.pop();
			if (curr->left != nullptr)
				q.push(curr->left);
			if (curr->right != nullptr)
				q.push(curr->right);
		}
		for (const auto& i : levelVals)
			std::cout << i << "  ";
		std::cout << "\n";
	}
}


void TestBST() {
	BST t;
	std::vector<int> arr{ 8,6,5,3,0,1,3,2 };
	for (const auto& i : arr)
		t.insert(i);

	//showInorder(t.root);
	showInorderIterative(t.root);
	nodeBst res(-999);
	convertBstToIncreasingOrder(t.root, res);
	auto resNode = res.right;
	while (resNode != nullptr)
	{
		std::cout << resNode->val << "  ";
		resNode = resNode->right;
	}
}