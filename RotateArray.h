#pragma once
#include "common.h"


void RotateArray(std::vector<int>& arr, int k)
{
	std::reverse(arr.begin(), arr.end());
	std::reverse(arr.begin() + k, arr.end());
	std::reverse(arr.begin(), arr.begin() + k);
}


void TestRotateArr() {

	PRINTTESTFUNCINFO();

	std::vector<int>arr{ 1,2,3,4,5,6,7 };
	RotateArray(arr, 3);
	for (const auto& i : arr)
		std::cout << i << "  ";
	std::cout << "\n";
}