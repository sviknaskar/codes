#pragma once
#include <iostream>
#include <variant>

struct t1 {
	void show()
	{
		std::cout << str <<"\n";
	}

	std::string str = "t1";
};

struct t2 {
	void show()
	{
		std::cout << str << "\n";
	}
	std::string str = "t2";
};

struct t3 {
	void show()
	{
		std::cout << str << "\n";
	}
	std::string str = "t3";
};


struct strChanger {
	void operator()(std::shared_ptr<t3>& o) {
		o->str += "  Hello Hello ############";
	}

	template<typename T>
	void operator()(T& o) {
		o->str += "  Hello Hello";
	}
};


void testVisitor()
{
	std::variant<std::shared_ptr<t1>, std::shared_ptr<t2>, std::shared_ptr<t3>> classTypes;

	using type = t2;
	classTypes = std::shared_ptr<type>(new type);
	
	std::visit(strChanger{}, classTypes);
	
	std::get<std::shared_ptr<type>>(classTypes)->show();
}