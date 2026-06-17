#pragma once
#include "common.h"


bool dfs(std::vector<std::vector<char>>& board, const std::string& word, int r, int c, int idx, int rows, int cols) {
	if (idx == word.size())
		return true;
	if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != word[idx])
		return false;
	auto tmp = board[r][c];
	board[r][c] = '#';
	bool found = dfs(board, word, r-1, c, idx+1, rows, cols) || dfs(board, word, r+1, c, idx + 1, rows, cols) 
					|| dfs(board, word, r, c - 1, idx + 1, rows, cols) || dfs(board, word, r, c + 1, idx + 1, rows, cols);

	board[r][c] = tmp;
	return found;
}

bool findWord(std::vector<std::vector<char>>& board, std::string word) {
	int rows = board.size();
	int cols = board[0].size();
	for (int r = 0; r < rows; r++) {
		for (int c = 0; c < cols; c++) {
			if (board[r][c] == word[0]) {
				return dfs(board, word, r, c, 0, rows, cols);
			}
		}
	}
	return false;
}


void FoundWordTest() {
	std::vector<std::vector<char>> board = { {'B', 'L', 'C', 'H'},{'E', 'E', 'L', 'T'},{'D', 'A', 'K', 'A'}, };
	std::string word = "BLEEDAK";
	bool found = findWord(board, word);
	std::cout << "word found: " << found;
}