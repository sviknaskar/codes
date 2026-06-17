#pragma once
#include "common.h"
#include <queue>
#include <unordered_map>


int getKFreqElem(const std::vector<int>& arr, int k)
{ 
	std::unordered_map<int, int> freq;
	for (const auto& i : arr)
		freq[i]++;

	int maxFreq = -1;
	
	for (const auto& i : freq) {
		std::cout << i.first << "   " << i.second << "\n";
		maxFreq = std::max(maxFreq, i.second);
	}
	std::vector<std::vector<int>> bucket(maxFreq+1);
	for (const auto& i : freq)
		bucket[i.second].push_back(i.first);

	return 0;
}


void TestKFrequentElem()
{
	std::vector<int> arr;
	for (int i = 0; i < 15; i++)
		arr.push_back(genRandomInRange(1,5));

	for (const auto& i : arr)
		std::cout << i << "  ";
	std::cout << "\n";

	getKFreqElem(arr, 3);
}
