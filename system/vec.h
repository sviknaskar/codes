#pragma once
#include <iostream>

template<typename T>
struct vec {
	vec() {
		buff = new T[capacity];
	}

	void pushBack(T v) {
		checkForBuffcapacity();
		buff[currPos++] = v;
		++size;
	}

	void checkForBuffcapacity() {
		if (size == capacity)
		{
			//std::cout << "capacity increased "<<capacity<<"->"<<2*capacity<<"\n";
			capacity *= 2;
			T* tmpBuff = new T[capacity];
			memcpy(tmpBuff, buff, capacity * sizeof(T));
			delete[] buff;
			buff = tmpBuff;
			
		}
		
	}


	~vec()
	{
		delete[] buff;
	}


	void show() const
	{
		for (size_t i = 0; i < size; i++)
			std::cout << buff[i] << "  ";

		std::cout << "\n";
	}


	T* begin()
	{
		return buff;
	}

	T* end()
	{
		return buff + size;
	}

	T* buff = nullptr;
	int capacity = 3;
	int size = 0;
	int currPos = 0;
	
};



void vecTest()
{
	vec<int> v;
	for (int i = 0; i < 80; i++)
		v.pushBack(i);


	auto i = v.begin();
	std::cout << *(i) << "\n";


	auto e = v.end() - 1;
	std::cout << *e << "\n";

	//v.show();
}