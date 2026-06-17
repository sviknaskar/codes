#pragma once
#include "common.h"


int deleteDuplicateSortedList(std::vector<int>& arr)
{

	// Modifies the array with the unique elements at the begining of the array. returns total numbers of unique elements.

	if (arr.size() == 0)
		return -1;
	size_t idx = 0;
	for (size_t i = 0; i < arr.size() - 1; i++)
	{
		if (arr[idx] != arr[i]) {
			idx++;
			arr[idx] = arr[i];
		}
			
	}
	return idx + 1;
}


void TestDeleteDuplicateSortedList() 
{
	PRINTTESTFUNCINFO();
	std::vector<int> arr{ 1, 1, 1, 2, 2, 4, 5, 5, 6, 6 };
	int r = deleteDuplicateSortedList(arr);
	
	std::cout << "idx: " << r << "\n";
	for (const auto& i : arr)
		std::cout << i << "  ";

}