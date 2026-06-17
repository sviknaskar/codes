#include "common.h"
#include <bit>

bool isLittleEndian()
{ 
	int x = 1;
	char* c = reinterpret_cast<char*>(&x);
	if (*c == 1)
		return true;
	return false;
}



bool isEven(int n)
{
	return !(n&1);
}


int countSetBits(int n)
{
	int count = 0;
	while (n)
	{
		n &= (n - 1);
		count++;
	}
	return count;
}

int findMissingNum(const std::vector<int> arr) {
	int ans = arr.size();
	for (int i = 0; i < arr.size(); i++)
	{
		ans ^= i;
		ans ^= arr[i];
	}
	return ans;
}


int reverseBits(uint32_t n) {
	int ans = 0;
	for (int i = 0; i < 32; i++)
	{
		ans <<= 1;
		if (n & 1)
			ans |= 1;
		n >>= 1;
	}
	return ans;
}