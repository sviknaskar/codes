#include "common.h"
#include <fstream>

struct testClass {
	void test() {
		std::cout << "this is from void test\n";
	}
};

struct readerWriter {
	readerWriter() {
		//file.open("test2.txt");
	}
	void read(const std::string& threadName) {
		while (!finished) {
			std::unique_lock<std::mutex> lk(mtx);
			while (writing) {
				cv.wait(lk);
			}
			//std::cout << "reading from " << threadName<<"\n";
			std::cout << "reading  shared value: " << sharedValue << "\n";
			std::this_thread::sleep_for(std::chrono::milliseconds(10));
			lk.unlock();
			cv.notify_all();
				
		}
	}
	void write() {
		while (!finished) {
			std::unique_lock<std::mutex>lk(mtx);
			while (writing) {
				cv.wait(lk);
			}
			count++;
			sharedValue++;
			std::cout << "writing value after writing: "<< sharedValue<<"\n";
			std::this_thread::sleep_for(std::chrono::milliseconds(100));
			//file << std::to_string(count) << "\n";
			lk.unlock();
			cv.notify_one();
			if (count == 5) {
				finished = true;
			}
		}
	}
	~readerWriter() {
		//file.close();
	}

	std::mutex mtx;
	std::condition_variable cv;
	bool writing = false;
	int count = 0;
	bool finished = false;
	int sharedValue = 0;
	//std::ofstream file;
};

void readerWriterTest() {
	readerWriter rw;
	std::thread tr1(&readerWriter::read, &rw, "readThreadOne");
	std::thread tr2(&readerWriter::read, &rw, "readThreadTwo");
	std::thread tw1(&readerWriter::write, &rw);
	tr1.join();
	tr2.join();
	tw1.join();
	testClass tc;
	std::thread t1(&testClass::test, &tc);
	t1.join();


	//std::ofstream file;
	//file.open("test.txt");
	//file << "123\n";
	//file.close();
}