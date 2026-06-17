#pragma once
#include "common.h"

int SearchRotatedArr(const std::vector<int>& arr, int target)
{
	size_t first = 0;
	size_t last = arr.size()-1;
	while (first != last)
	{
		const size_t mid = first + (last - first) / 2;
		if (arr[mid] == target)
			return mid;
		if (arr[first] <= arr[mid])
		{
			if (arr[first] <= target && target < arr[mid])
				last = mid;
			else
				first = mid + 1;
		}
		else
		{
			if (arr[mid] <= target && target < arr[last - 1])
				first = mid + 1;
			else
				last = mid;
		}	
	}
	return -1;
}


int searchRotatedArr2(const std::vector<int>& arr, int target)
{
	int left = 0;
	int right = arr.size() - 1;
	while (left <= right)
	{
		int mid = left + (right - left) / 2;
		if (arr[mid] == target)
			return mid;

		//see if left part is sorted
		if (arr[left] <= arr[mid])
		{
			if (arr[left] <= target && target < arr[mid])
				right = mid - 1;
			else
				left = mid + 1;
		}
		//else right part must be sorted
		else
		{
			if (arr[mid] < target && target < arr[right])
				left = mid + 1;
			else
				right = mid - 1;
		}
	}
	return -1;
}



int binSearch(const std::vector<int>& arr, int target, int begin, int end)
{
	while (begin < end)
	{
		int mid = begin + (end - begin) / 2;
		if (target == arr[mid])
			return mid;
		if (arr[mid] > target)
			end = mid - 1;
		else
			begin = mid + 1;
	}
	return -1;
}



int findPivot(const std::vector<int>& arr)
{
	int begin = 0;
	int end = arr.size()-1;
	while (begin < end)
	{
		if (arr[begin] < arr[end])
			return begin;

		int mid = (end + begin) / 2;
		if (arr[mid] > arr[end])
			begin = mid + 1;
		else
			end = mid;
	}
}


int SerchInRotTree(const std::vector<int>& arr, int target)
{
	int pivot = findPivot(arr);
	//std::cout << pivot << "\n";
	if (arr[pivot] == target)
		return pivot;

	if (pivot == 0)
		return binSearch(arr, target, 0, arr.size() - 1);
	if (arr[0] <= target)
		return binSearch(arr, target, 0, pivot);
	else
		return binSearch(arr, target, pivot, arr.size() - 1);


	return -1;
}


void TestSearchRotatedArr()
{
	PRINTTESTFUNCINFO();
	std::vector<int> arr{ 67, 70, 77, 82, 5, 8, 34, 66 };
	//int pos = SearchRotatedArr(arr, 66);
	
	//int pos = SerchInRotTree(arr, 34);

	int pos = searchRotatedArr2(arr, 67);
	std::cout << pos << "\n";
}