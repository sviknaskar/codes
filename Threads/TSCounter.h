#pragma once
#include <thread>
#include <mutex>
//#include <condition_variable>
#include <chrono>
#include <vector>
#include <iostream>


using namespace std::chrono_literals;

#define MAXCOUNT (30)

struct TSCounter {

	void increment(int threadIdx) {
			std::unique_lock<std::mutex>lk(mtx);
			count+=threadIdx;
			std::cout << "incrementing from " << threadIdx << " thread id: " << std::this_thread::get_id() << "  count: " << count << "\n";
			std::this_thread::sleep_for(1000ms);
	}

	int getCount(){
		std::unique_lock<std::mutex>lk(mtx);
		return count;
	}
private:
	std::mutex mtx;
	int count = 0;
};


void TestTSCounter()
{
	TSCounter tsc;
	std::vector<std::thread> tVec;
	constexpr int numThreads = 20;
	for (int i = 0; i < numThreads; i++)
		tVec.emplace_back(&TSCounter::increment, &tsc, i);
	for (int i = 0; i < numThreads; i++)
		tVec[i].join();
}