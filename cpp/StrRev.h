#pragma once
#include "common.h"

void revString(std::string& s)
{
	int left = 0;
	int right = s.size() - 1;
	auto c = s[left];
	while (left < right) {
		std::swap(s[left++], s[right--]);
	}
}

void TestStrRev()
{
	PRINTTESTFUNCINFO();
	std::string s = "Hello World";
	revString(s);
	std::cout << s << "\n";
}