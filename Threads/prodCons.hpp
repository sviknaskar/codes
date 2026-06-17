#pragma once

#include <thread>
#include <mutex>
#include <condition_variable>
#include <chrono>
#include <queue>
#include <iostream>

using namespace std::chrono_literals;


struct ProdCons {

	void prod() {
		//while (true)
		for(idx = 0; idx< maxProduce;idx++)
		{
			std::unique_lock<std::mutex> lk(mtx);
			while (sharedBuff.size() >= maxSize)
				condVar.wait(lk);
			std::cout << "produceing " << idx << "\n";
			sharedBuff.push(idx);
			//idx++;
			condVar.notify_one();

			/*if (idx > maxProduce)
				break;*/

		}
	}
	void cons() {
		while (1)
		{
			std::unique_lock<std::mutex> lk(mtx);
			while (sharedBuff.empty())
			{
				std::cout << "waiting for producer\n";
				std::this_thread::sleep_for(2000ms);
				condVar.wait(lk);
			}

			auto i = sharedBuff.front();
			std::cout << "consumed " << i << "\n";
			sharedBuff.pop();

			lk.unlock();
			condVar.notify_one();
			if (i >= maxProduce-1)
			{
				std::cout << "finished consuming " << maxProduce << " tasks\n";
				break;
			}
				
		}
	}


	std::mutex mtx;
	std::condition_variable condVar;
	std::queue<int> sharedBuff;
	int maxSize = 5;
	int maxProduce = 17;
	int idx = 0;
};



void testProdCons() {
	/*std::thread thProd(produce);
	std::thread thCons(consume);

	thProd.join();
	thCons.join();*/

	ProdCons pc;
	std::thread thProd(&ProdCons::prod, &pc);
	std::thread thCons(&ProdCons::cons, &pc);

	thProd.join();
	thCons.join();
}