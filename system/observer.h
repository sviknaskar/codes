#pragma once
#include <iostream>
#include <vector>
#include <map>



class observer {
public:
	virtual void update(int) = 0;
	virtual ~observer() {}
};



class subject {
public:
	//subject() {}
	virtual void addObserver(std::shared_ptr<observer>) = 0;
	virtual void removeObserver(const int) = 0;
	virtual void notifyObservers() = 0;
	virtual ~subject() {}
};


class idGenerator
{
public:
	static int currId;
	int getId()
	{
		return currId++;
	}
};
int idGenerator::currId = 0;


class info
{
public:
	info() :a(1), b(2), c(3) {}
	int a, b, c;
};


class concreteSubject :public subject {
public:	
	//concreteSubject() {}
	void addObserver(std::shared_ptr<observer> op) override{
		observers.insert(std::make_pair(g.getId(), op));
		//std::cout << "break\n";
	}
	void removeObserver(const int)  override {}
	void notifyObservers()  override {
		for (auto& i : observers)
		{
			switch (i.first % 3)
			{
				case 0:
					i.second->update(in.a);
					break;
				case 1:
					i.second->update(in.b);
					break;
				case 2:
					i.second->update(in.c);
					break;
			}
			
		}
			
	}
	~concreteSubject() {}

	std::map<int, std::shared_ptr<observer>> observers;
	info in;
	idGenerator g;
};


class concreteObserver1 :public observer {
public:	
	void update(int x)override { v = x + 10; }
	~concreteObserver1() {}
	int v;
};

class concreteObserver2 :public observer {
public:
	void update(int x)override { v = x + 20; }
	~concreteObserver2() {}
	int v;
};

class concreteObserver3 :public observer {
public:
	void update(int x)override { v = x + 30; }
	~concreteObserver3() {}
	int v;
};



void observerTest()
{
	/*idGenerator g;
	for (int i = 0; i < 5; i++)
		std::cout << g.getId() << "\n";*/

	concreteSubject s;

	std::shared_ptr<observer> ob1(new concreteObserver1);
	std::shared_ptr<observer> ob2(new concreteObserver2);
	std::shared_ptr<observer> ob3(new concreteObserver3);


	s.addObserver(ob1);
	s.addObserver(ob2);
	s.addObserver(ob3);
	s.notifyObservers();
	

	auto x1 = dynamic_cast<concreteObserver1*>(ob1.get());
	auto x2 = dynamic_cast<concreteObserver2*>(ob2.get());
	auto x3 = dynamic_cast<concreteObserver3*>(ob3.get());
	std::cout << x1->v << "         " << x2->v << "         " << x3->v << "\n";

}