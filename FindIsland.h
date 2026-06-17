#pragma once
#include "common.h"

void dfs(std::vector<std::vector<int>>& mat, int r, int c, int rows, int cols) {
	if (r < 0 || r >= rows || c < 0 || c >= cols || mat[r][c] == 0)
		return;
	mat[r][c] = 0;
	dfs(mat, r - 1, c, rows, cols);
	dfs(mat, r + 1, c, rows, cols);
	dfs(mat, r, c - 1, rows, cols);
	dfs(mat, r, c + 1, rows, cols);
}


int findIsland(std::vector<std::vector<int>> mat) {
	int count = 0;
	int rows = mat.size();
	int cols = mat[0].size();
	
	
	for (int r = 0; r < rows; r++) {
		for (int c = 0; c < cols; c++) {
			if (mat[r][c] == 1) {
				dfs(mat, r, c, rows, cols);
				count++;
			}
		}
	}
	
	return count;
}


void FindIslandsTest() {
	std::vector<std::vector<int>> mat = { {1, 1, 0, 0, 0},
		{0, 1, 0, 0, 1},
		{1, 1, 0, 1, 1 },
		{0, 0, 0, 1, 0},
		{1, 0, 1, 1, 1 }};

	int res = findIsland(mat);
	std::cout << "total number of islands: " << res;
 }