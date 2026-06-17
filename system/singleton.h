#pragma once
#include <iostream>



struct singleton {
public:
	static singleton& get()
	{
		static singleton instance;
		return instance;
	}
	singleton(const singleton&) = delete;
	singleton& operator=(const singleton&) = delete;
	
	void setval(int v = 100)
	{
		x = v;
	}
	int getVal() const{
		return x;
	}
private:
	singleton() = default;
	int x = 7;
};

void testSingleton()
{
	//singleton *s;
	std::unique_ptr<singleton>s;
	singleton& i = s->get();
	int x = i.getVal();
	std::cout << x << "\n";
	i.setval();
	std::unique_ptr<singleton>s1;
	singleton& i2 = s->get();
	x = i2.getVal();
	std::cout << x << "\n";
	i2.setval(6);
	x = i.getVal();
	std::cout << x << "\n";
}