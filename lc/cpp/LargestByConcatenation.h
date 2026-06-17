#pragma once
#include "common.h"
#include <string>
void getLargestNumberByConcatenation(const std::vector<int>& arr) 
{
	auto compareFunc = [](const std::string& str1, const std::string& str2)->bool {
		return str1 + str2 > str2 + str1;
		};

	//std::cout << compareFunc("2", "30") << " \n";
	std::vector<std::string> numStr;
	

	for (int i : arr)
		numStr.push_back(std::to_string(i));

	std::sort(numStr.begin(), numStr.end(), compareFunc);

	std::string s = "";
	if (numStr[0] == "0") {
		s = "0";
		return;
	}
	for (const auto& i : numStr)
		//std::cout << i << " ";
		s += i;
	std::cout << s << "\n";


}

void TestLargestByConcatenation() {
	std::vector<int> arr{ 3, 30, 34, 5, 9 };
	getLargestNumberByConcatenation(arr);
}