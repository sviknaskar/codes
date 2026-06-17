#pragma once
#include "common.h"
#include "LL.h"

void revLL(llist& l)
{
	auto curr = l.head;
	std::shared_ptr<listNode> prev, next;
	while (curr != nullptr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	l.head = prev;
}


void TestLLReverse()
{
	llist l;
	for (int i = 0; i < 10; i++)
		l.insert(genRandomInRange());

	l.show();
	revLL(l);
	l.show();
}