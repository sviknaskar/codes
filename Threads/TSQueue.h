#pragma once
#include "common.h"

#include <queue>
#include <vector>

struct TSQueue {
	TSQueue() = default;
	void push(int val) {
		std::unique_lock<std::mutex> lk(mtx);
		std::cout << "inserted " << val << "\n";
		buff.push(val);
		cv.notify_all();
	}
	int pop() {
		std::unique_lock<std::mutex> lk(mtx);
		while (buff.empty())
			cv.wait(lk);
		auto v = buff.front();
		buff.pop();
		std::cout << "popped " << v << "\n";
		return v;
	}

	void show()
	{
		std::unique_lock<std::mutex> lk(mtx);
		auto tmpQueue = buff;
		while (!tmpQueue.empty())
		{
			int v = tmpQueue.front();
			std::cout << v << "  ";
			tmpQueue.pop();
		}
		std::cout << "\n";
	}

private:
	std::queue<int> buff;
	std::condition_variable cv;
	std::mutex mtx;
};



void TestTSQueue()
{
	TSQueue q;

	int numInsertThread = 10;
	std::vector<std::thread> pushBuff, popBuff;

	for (int i = 0; i < numInsertThread; i++) {
		pushBuff.emplace_back(&TSQueue::push, &q, i + 10);
		popBuff.emplace_back(&TSQueue::pop, &q);
	}
		
/*
	std::thread t1(&TSQueue::push, &q, 10);
	std::thread t2(&TSQueue::push, &q, 11);
	std::thread t3(&TSQueue::push, &q, 12);

	std::thread t4(&TSQueue::pop, &q);

	t1.join();
	t2.join();
	t3.join();
	t4.join();
*/

	for (int i = 0; i < numInsertThread; i++) {
		pushBuff[i].join();
		popBuff[i].join();
	}
		

	q.show();
}