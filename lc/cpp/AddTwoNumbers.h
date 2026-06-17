#pragma once
#include "common.h"
#include "LL.h"


void addTwoNumbers(llist& num1, llist& num2)
{
	int carry = 0;
	llist resList;
	int largerNum = 1;
	auto h1 = num1.head;
	auto h2 = num2.head;
	while (true)
	{
		if (h1 == nullptr || h2 == nullptr)
		{
			if (h2 == nullptr)
				largerNum = 2;
			break;
		}
			
		int res = h1.get()->num + h2.get()->num + carry;
		carry = res / 10;
		res %= 10;
	
		//std::cout << res << "  ";

		resList.insert(res);
		h1 = h1.get()->next;
		h2 = h2.get()->next;
	}

	if (carry > 0)
		resList.insert(carry);

	std::cout << "\n";
	resList.show();
}

void TestAddTwoNumbers()
{ 
	llist num1;
	num1.insert(2);
	num1.insert(4);
	num1.insert(3);
	num1.show();

	std::cout << "\n";

	llist num2;
	num2.insert(5);
	num2.insert(6);
	num2.insert(9);
	num2.show();

	addTwoNumbers(num1, num2);
}