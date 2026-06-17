#pragma once
#include <vector>
#include <queue>
#include "BST.h"

struct data {
	data() = default;
	data(BST::nodeBST* n, size_t s, size_t e) {
		node = n;
		start = s;
		end = e;
	}
	BST::nodeBST* node;
	int start, end;
};



BST getBSTFromSortedArray(std::vector<int> arr)
{
	BST t;
	if (arr.size() == 0)
		return t;

	
	std::queue<data> q;
	auto newRoot = new BST::nodeBST(0);
	q.push(data(newRoot, 0, arr.size()-1));
	while (!q.empty())
	{
		auto d = q.front();
		q.pop();
		auto curr = d.node;
		int start = d.start;
		int end = d.end;
		int mid = (start + end) / 2;
		curr->val = arr[mid];

		if (start <= mid - 1)
		{
			curr->left = new BST::nodeBST(0);
			q.push(data(curr->left, start, mid - 1));
		}

		if (mid + 1 <= end)
		{
			curr->right = new BST::nodeBST(0);
			q.push(data(curr->right, mid + 1, end));
		}
	}
	t.root = newRoot;
	return t;
}


void TestSortedArrToBst() {
	std::vector<int>arr;
	for (int i = 0; i < 10; i++) {
		int x = genRandomInRange();
		//std::cout << x << "  ";
		arr.push_back(x);
	}

	std::sort(arr.begin(), arr.end());
	for (const auto& i : arr)
		std::cout << i << " ";

	auto t = getBSTFromSortedArray(arr);
	std::cout << "\n";
	showInorderIterative(t.root);
	//showPreorder(t.root);
}