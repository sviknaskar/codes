#pragma once
#include "common.h"

void strShiftK(std::string str, int k)
{
	std::reverse(str.begin(), str.end());
	
	std::reverse(str.begin(), str.begin() + 4);
	std::reverse(str.begin()+4, str.end());
	std::cout << str << "\n";
}


void TestStrShift() {
	std::string str = "helloworld";
	strShiftK(str, 4);
}