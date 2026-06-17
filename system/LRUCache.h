#pragma once
#include "common.h"
struct LRUCache {
public:
	LRUCache(int cv) :capacity(cv) {}
	int get(int key) {
		if (cacheMap.find(key) == cacheMap.end())
			return -1;
		cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
		cacheMap[key] = cacheList.begin();
		return cacheMap[key]->value;
	}
	void set(int key, int val) {
		if (cacheMap.find(key) == cacheMap.end())
		{
			//remove least recently used entry if capacity exists
			if (cacheList.size() == capacity)
			{
				cacheMap.erase(cacheList.back().key);
				cacheList.pop_back();
			}
			cacheList.push_front(CacheNode(key, val));
			cacheMap[key] = cacheList.begin();
		}
		else
		{
			cacheMap[key]->value = val;
			cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
			cacheMap[key] = cacheList.begin();
		}
	}
private:
	struct CacheNode {
		int key;
		int value;
		CacheNode(int k, int v) :key(k), value(v) {}
	};
	std::list<CacheNode> cacheList;
	std::unordered_map<int, std::list<CacheNode>::iterator> cacheMap;
	int capacity;
};


void TestLRUCache()
{
	
	PRINTTESTFUNCINFO();
	LRUCache lruc(3);
	lruc.put(1, 1);
	lruc.put(2, 2);
	lruc.put(3, 3);
	lruc.show();
	std::cout << "after access\n";
	lruc.get(1);
	lruc.show();
	lruc.put(4, 4);
	lruc.put(5, 5);
	std::cout << "after insert\n";
	lruc.show();
	
}