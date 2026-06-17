#pragma once
#include "common.h"


std::optional<int> getLenLongestConsecutiveSeq(const std::vector<int>& arr, std::vector<int>& seq)
{
	if (arr.size() == 0)
		return {};

	std::unordered_map<int, bool> used;
	for (const auto& i : arr)
		used[i] = false;

	int longest = 1;

	for (const auto& i : arr)
	{
		if (used[i])
			continue;
		
		std::vector<int> tmpSeq{i};
		used[i] = true;
		int len = 1;
		int j = i+1;
		while (used.find(j) != used.end()) {
			used[j] = true;
			len++;
			tmpSeq.push_back(j);
			j++;
		}

		j = i - 1;
		while (used.find(j) != used.end()) {
			used[j] = true;
			len++;
			tmpSeq.push_back(j);
			j--;
		}

		if (len > longest)
		{
			seq.clear();
			seq = tmpSeq;
		}
		longest = std::max(longest, len);
	}
	return longest;
}

void TestLongestConsecutiveSeq()
{
	PRINTTESTFUNCINFO();
	std::vector<int> arr{ 8, 2, 1, 6, 3, 11, 10, 18, 99, 65, 13, 90, 14, 67, 15, 9};
	std::vector<int> seq;
	auto res = getLenLongestConsecutiveSeq(arr,seq);
	std::cout << res.value_or(-1) << "\n";
	for (const auto& i : seq)
		std::cout << i << "  ";
}