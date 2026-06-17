#pragma once
#include "common.h"


void genImage(std::vector<std::vector<int>>& image, int height = 5, int width = 5)
{
	for (int i = 0; i < height; i++) {
		std::vector<int>rowVec;
		for (int j = 0; j < 5; j++)
			rowVec.push_back(genRandomInRange());
		image.push_back(rowVec);
	}
}


void RotateImage(std::vector<std::vector<int>>& image)
{
	int row = image.size();
	int col = image[0].size();
}


void TestImageRotate()
{
	PRINTTESTFUNCINFO();
	std::vector<std::vector<int>> img;
	genImage(img);
	for (const auto& i : img) {
		for (const auto& j : i)
			std::cout << j << "  ";
		std::cout << "\n";
	}
		

}