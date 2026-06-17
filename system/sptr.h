#pragma once


template<typename T>
struct sptr {
public:

	sptr(T* vp = nullptr) :ptr(vp) {
		if (vp == nullptr)
			refCount = new int(0);
		else 
			refCount = new int(1);
	}
	sptr(const sptr& o){
		ptr = o.ptr;
		refCount = o.refCount;
		if (o.ptr != nullptr)
			(*refCount)++;
	}
	sptr& operator=(const sptr& o){
		ptr = o.ptr;
		refCount = o.refCount;
		if (o.ptr != nullptr)
			++(*refCount);
	}

	int getCount()const
	{
		return *refCount;
	}

	T* get()const
	{
		return ptr;
	}

	T* operator->()const
	{
		return ptr;
	}

	T& operator*()const
	{
		return *ptr;
	}

	~sptr() {
		if (*refCount == 0)
		{
			if (ptr != nullptr)
				delete ptr;
			ptr = nullptr;
			delete refCount;
		}
		else
			*refCount--;
	}
private:
	T* ptr;
	int* refCount = nullptr;
};


struct box {
	box() :x(10), y(20), w(100), h(150) {}
	int x;
	int y;
	int w;
	int h;
};


void sptrTest()
{
	sptr<box> bp1(new box);
	std::cout << bp1.getCount() << "\n";
	auto bp2 = bp1;
	std::cout << bp1.getCount()<<"    "<<bp2.getCount() << "\n";
}