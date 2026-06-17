def wordSearch(mat, w):
    rows = len(mat)
    cols = len(mat[0])
    def dfs(r, c, idx):
        if idx == len(w):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or mat[r][c] != w[idx]:
            return False

        tmp = mat[r][c]
        mat[r][c] = '$'

        found = (dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1) or dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1))

        mat[r][c] = tmp
        return found

    idx = 0
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == w[idx]:
                return dfs(i,j,idx)
    return False


def TestFindWord():
    board = [
        ['B', 'L', 'C', 'H'],
        ['E', 'E', 'L', 'T'],
        ['D', 'A', 'K', 'A'],
    ]
    word = "BLEEDAK"

    res = wordSearch(board, word)
    print(res)

TestFindWord()