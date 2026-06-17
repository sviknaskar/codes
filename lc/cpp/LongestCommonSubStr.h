#pragma once
#include "common.h"


std::pair<int, int> longestCommonSubStr(const std::string& str1, const std::string& str2)
{
	int l1 = str1.size();
	int l2 = str2.size();

	std::vector<int> prev(l1 + 1, 0);
	int res = 0;
	int startPos = 0;
	for (int i = 0; i < l2; i++)
	{
		std::vector<int> curr(l1 + 1, 0);
		for (int j = 0; j < l1; j++) {
			if (str1[j] == str2[i]) {
				curr[j+1] = prev[j] + 1;
			}
		}

		auto it = std::max_element(curr.begin(), curr.end());
		auto loc = it - curr.begin();
		if (res < *it) {
			res = std::max(res, *it);
			startPos = loc - res;
			std::cout << "maxLoc: " << loc<<"     ";
		}
		for (const auto& i : curr)
			std::cout << i << "   ";
		std::cout << "\n";

		prev = curr;
	}
	return std::make_pair(startPos+1, res);
}


void TestlongestCommonSubStr() {
	PRINTTESTFUNCINFO();
	std::string str1 = "hjlgsgjbsdb";
	std::string str2 = "sgjbs";
	auto res = longestCommonSubStr(str1, str2);
	std::cout << "longest common sub string length: " << res.second << "   start location:" << res.first << "\n";
}