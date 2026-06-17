#pragma once
#include "common.h"



void showMatrixSpiral(const std::vector<std::vector<int>>& mat) {
	int rows = mat.size();
	int cols = mat[0].size();

	int top = 0;
	int bottom = rows - 1;
	int left = 0;
	int right = cols - 1;

	while (top <= bottom && left <= right)
	{
		//top row
		for (int i = left; i <= right; i++)
			std::cout << mat[top][i] << "  ";
		top++;

		//right col
		for (int i = top; i <= bottom; i++)
			std::cout << mat[i][right] << "  ";
		right--;

		//bottom row
		if (top <= bottom)
		{
			for (int i = right; i >= left; i--)
				std::cout << mat[bottom][i] << "  ";
			bottom--;
		}
		

		//left col
		if (left <= right)
		{
			for (int i = bottom; i >= top; i--)
				std::cout << mat[i][left] << "  ";
			left++;
		}
		
	}
}


void TestSpiralMatrix() {
	std::vector<std::vector<int>> mat{ {1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16} };
	showMatrixSpiral(mat);
}