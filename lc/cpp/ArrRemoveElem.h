#pragma once
#include "common.h"


int removeElemFromArr(std::vector<int>& arr, int elem)
{
	int idx = 0;
	for (int i = 0; i < arr.size(); i++)
	{
		if (arr[i] != elem)
		{
			arr[idx] = arr[i];
			idx++;
		}
	}
	return idx;
}


void TestArrRemoveElement()
{
	PRINTTESTFUNCINFO();

	std::vector<int> arr{ 0, 1, 2, 0, 4, 5, 0, 6, 7, 0 };
	int newLen = removeElemFromArr(arr, 0);
	std::cout << "New Length: " << newLen << "\n";
	for (const auto& i : arr)
		std::cout << i << "  ";

}