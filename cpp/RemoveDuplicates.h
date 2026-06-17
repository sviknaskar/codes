#pragma once
#include "common.h"
int removeDuplicates(std::vector<int>& arr)
{ 
	std::unordered_map<int, bool> hashMap;
	int idx = 0;
	std::vector<int>unique;
	for (int i = 1; i < arr.size(); i++)
	{
		if (hashMap.find(arr[i]) != hashMap.end())
			continue;
		else {
			arr[idx++] = arr[i];
			hashMap.insert({ arr[i], true });
			unique.push_back(arr[i]);
		}
	}

	/*std::cout << "from functions\n";
	for (const auto& i : unique)
		std::cout << i << "  ";
	std::cout << "\n";*/

	return idx;
}



void TestRemoveDuplicates() {
	PRINTTESTFUNCINFO();
	std::vector<int> arr;
	for (int i = 0; i < 100; i++)
		arr.push_back(genRandomInRange(1, 10));

	for (const auto& i : arr)
		std::cout << i << "  ";
	std::cout << "\n";
	int e = removeDuplicates(arr);
	for (int i = 0; i < e; i++)
		std::cout << arr[i] << "  ";
	std::cout << "\n";
}