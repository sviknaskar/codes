#pragma once
#include "common.h"

int getMajorityElem(const std::vector<int>& arr) {
	std::unordered_map<int, int>ht;
	for (const auto& i : arr)
	{
		if (ht.find(i) == ht.end())
			ht[i] = 1;
		else
			ht[i]++;
	}

	for (const auto& i : ht)
		std::cout << i.first << "    " << i.second << "\n";

	std::cout << "\n";

	int maxElem = -1;

	if (!ht.empty()) {
		auto it = std::max_element(ht.begin(), ht.end(),
			[](const std::pair<int, int>& x, const std::pair<int, int>& y) {
				return x.second < y.second;
			});
		maxElem = it->first;
	}
	return maxElem;
}



void TestMajorityElem()
{
	std::vector<int>arr;
	for (int i = 0; i < 10; i++)
	{
		arr.push_back(genRandomInRange(1, 5));
	}

	for (const auto& i : arr)
		std::cout << i << "  ";
	std::cout << "\n";
	auto majElem = getMajorityElem(arr);
	std::cout << "Majority Element: " << majElem;
}