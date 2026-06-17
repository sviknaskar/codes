#pragma once



std::vector<int> getKSum(std::vector<int>& arr, int target, int k=3)
{
	std::vector<int>res{};
	std::sort(arr.begin(), arr.end());
	
	//int sum = 0;
	//for (int i = 0; i < k; i++)
	//	sum += arr[i];

	//if (sum == target) {
	//	for (int j = 0; j < k; j++) {
	//		res.push_back(arr[j]);
	//	}
	//	return res;
	//}
	//	

	//for (int i = 1; i < arr.size() - k - 1; i++)
	//{
	//	//std::cout << i + k - 1 << "    " << i - 1 << "\n";
	//	sum += arr[i + k - 1] - arr[i - 1];
	//	if (sum == target) {
	//		for (int j = 0; j < k; j++) {
	//			res.push_back(arr[i + j - 1 ]);
	//		}
	//		break;
	//	}
	//}
	
	for (int i = 0; i < arr.size() - k - 1; i++)
	{
		int sum = 0;
		for (int j = 0; j < k; j++)
		{
			sum += arr[i + j];
		}
		if (sum == target)
			for (int j = 0; j < k; j++) {
				res.push_back(arr[i + j]);
			}
	}

	return res;
}


void TestKSum()
{
	PRINTTESTFUNCINFO();
	std::vector<int> arr{ 9,8,7,6,5,4,3,2,1 };
	auto r = getKSum(arr, 14, 4);
	if(r.size() != 0)
		for (const auto& i : r)
		std::cout << i << "  ";
}