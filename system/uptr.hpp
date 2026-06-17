#pragma once


template<typename T>
struct myunique {
public:
	myunique() : ptr(nullptr) {}
	myunique(T* vp) :ptr(vp) {}
	myunique(const myunique&) = delete;
	myunique& operator=(const myunique&) = delete;

	T* get() const {
		return ptr;
	}

	T& operator*() const
	{
		return *ptr;
	}

	T* operator->() const
	{
		return ptr;
	}

	T* release()
	{
		auto tmp = ptr;
		ptr = nullptr;
		return tmp;
	}

	~myunique()
	{
		if (ptr != nullptr)
			delete ptr;
		ptr = nullptr;
		
	}


private:
	T* ptr;
};



void myuniqueTest() {
	int* a = new int(10);
	myunique<int> ip(a);
	//myunique<int> ipC = ip;

	std::cout << *ip.get() << "\n";
}