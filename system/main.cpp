#include <iostream>
#include <random>
#include "virtInheritance.h"
#include "virtFunction.h"
#include "uptr.hpp"
#include "sptr.h"
#include "observer.h"
#include "visitor.h"
#include "cvOpsBank.h"
#include "vec.h"	
#include "singleton.h"
#include "setInsert.h"
#include "twoSum.h"
#include "validPalindrome.h"
#include "strstr.h"
#include "revWord.h"
#include "revNum.h"
#include "ll.h"
#include "Arr2dsmtptr.h"
#include "prodCons.hpp"
#include "asyncTest.h"
#include "DiningPhil.h"
#include "ReaderWriter.h"
#include "TSCounter.h"
#include "TSQueue.h"
#include "GenericFuncDef.h"

void genRand() {
	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution<>dis(1, 100);
	for (int i = 0; i < 10; i++)
	{
		std::cout << dis(gen) <<"\n";
	}
		
}


int main()
{
	//CPP, OOP and DS///////////////////////////
	//testVertInheritance();
	//myuniqueTest();
	//sptrTest();
	//observerTest();
	//testVisitor();
	//vecTest();
	//testSingleton();
	//genRand();	
	
	return 0;
}