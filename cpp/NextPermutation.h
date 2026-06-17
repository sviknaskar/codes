#pragma once
#include "common.h"


void getNextPermutation(std::vector<int>& arr)
{
	auto ri = arr.rbegin();
	int pivotIdx = 0;
	int count = 0;
	while (ri != arr.rend()-1  && *ri < *(ri + 1))
	{

		//std::cout << *ri << "  " << *(ri + 1) << "\n";
		count++;
		ri++;
	}
		
	pivotIdx = arr.size() - 1 - count - 1;
	int pivot = arr[pivotIdx];

	ri = arr.rbegin();
	count = 0;
	while (*ri < pivot)
	{

		//std::cout << *ri << "\n";
		count++;
		ri++;
	}
	int swapIdx = arr.size() - 1 - count ;
	//std::cout << swapIdx << "  " << arr[swapIdx] << "\n";
	std::swap(arr[pivotIdx], arr[swapIdx]);

	std::reverse(arr.begin() + pivotIdx + 1, arr.end());
}


void TestNextPermutation()
{
	std::vector<int> arr{ 6, 8, 7, 4, 3, 2 };

	getNextPermutation(arr);
	for (const auto& i : arr)
		std::cout << i << "  ";
}