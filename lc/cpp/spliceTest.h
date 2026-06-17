#pragma once
#include "common.h"


void TestSplice() {
	std::list l{ 1,2,3,4,5,6 };
	
	for (const auto& i : l)
		std::cout << i << "  ";

	std::cout << "\n";

	auto it = l.begin();

	auto dist = std::distance(it, l.end());

	std::advance(it, 3);

	l.splice(l.begin(), l, it);

	for (const auto& i : l)
		std::cout << i << "  ";
}