def findLand(mat):
    rows = len(mat)
    cols = len(mat[0])
    count = 0
    def dfs(r,c):
        if r<0 or r>=rows or c<0 or c >= cols or mat[r][c] == 0:
            return

        mat[r][c] = 0

        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 1:
                dfs(r,c)
                count += 1

    return count

def FindLandTest():
    mat = [[1, 1, 0, 0, 0],
           [0, 1, 0, 0, 1],
           [1, 1, 0, 1, 1],
           [0, 0, 0, 1, 0],
           [1, 0, 1, 1, 1]]

    count = findLand(mat)
    print(count)


FindLandTest()