#ifndef TWOSUM
#define TWOSUM
#include "common.h"

std::pair<int, int> getTwoSum(const std::vector<int>& arr, int target)
{
	std::unordered_map<int, int> buff;
	for (const auto& i : arr)
		buff[i] = i;
	std::pair<int, int> res = {};
	for (const auto& i : arr) {
		if (buff.find(target - i) != buff.end())
		{
			res = { i, target - i };
			break;
		}
	}
	return res;
}

void TestTwoSum()
{
	PRINTTESTFUNCINFO();

	std::vector<int> arr{ 1,2,3,4,5,6,7,8,9 };
	int target = 15;

	auto res = getTwoSum(arr, 15);
	std::cout << res.first << "  " << res.second << "\n";
}

#endif