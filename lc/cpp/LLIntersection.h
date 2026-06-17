#pragma once
#include "common.h"
#include "LL.h"


std::shared_ptr<listNode> getIntersectionPoint(const llist& l1, const llist& l2)
{
	auto ptr1 = l1.head;
	auto ptr2 = l2.head;

	if (ptr1 == nullptr || ptr2 == nullptr)
		return nullptr;

	while (ptr1 != ptr2)
	{
		ptr1 = ptr1 ? ptr1->next : l2.head;
		ptr2 = ptr2 ? ptr2->next : l1.head;
	}
	return ptr1;
}

void TestLLIntersection() {
	llist l1;
	l1.insert(10);
	l1.insert(11);
	l1.insert(12);
	l1.insert(13);


	llist l2;
	l2.insert(9);
	l2.insert(10);
	l2.head->next->next = l1.head->next;

	auto i = getIntersectionPoint(l1, l2);
	
	std::cout << "two lists intersecting at node: ";
	i->show();
	std::cout << "\n";
}