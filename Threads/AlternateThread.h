#pragma once
#include "common.h"

int num = -1;
std::mutex mtx;
std::condition_variable cv;

void increaseEven(const std::string& threadName ) {
	while (num < 100) {
		std::unique_lock<std::mutex> lk(mtx);
		while (num % 2 != 0)
			cv.wait(lk);
		num++;
		std::cout << threadName << "    " << num << "\n";
		cv.notify_all();
	}
}

void increaseOdd(const std::string& threadName) {
	while (num < 100) {
		std::unique_lock<std::mutex> lk(mtx);
		while (num % 2 == 0)
			cv.wait(lk);
		num++;
		std::cout << threadName << "    " << num << "\n";
		cv.notify_all();
	}
}

void alternateTest() {
	std::thread th1(increaseOdd, "odd");
	std::thread th2(increaseEven, "even");

	th1.join();
	th2.join();
}