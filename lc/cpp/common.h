#pragma once
#include <iostream>
#include <vector>
#include <optional>
#include <unordered_map>
#include <algorithm>
#include <random>
#include <limits>
#include <list>
#include <stack>
#include <queue>
#include <functional>
#include <string>


#define PRINTTESTFUNCINFO() std::cout << "TestName: " << __FUNCTION__ << "\n";



int genRandomInRange(const int low = 0, const int high = 20) {
	std::random_device rd;
	std::mt19937 mt(rd());
	std::uniform_int_distribution uid(low, high);
	return uid(mt);
}