def spiralMatrix(mat):
    rows = len(mat)
    cols = len(mat[0])
    left, top , right, bottom = 0, 0, cols-1, rows-1

    res = ""
    while left<=right and top<=bottom:

        #first row
        for i in range(left, right+1):
            res += str(mat[top][i])+"  "
        top += 1
        #last col
        for i in range(top, bottom+1):
            res += str(mat[i][right])+"  "
        right -= 1
        #last row
        for i in range(right, left-1, -1):
            res += str(mat[bottom][i])+"  "
        bottom -= 1
        #first col
        for i in range(bottom, top-1, -1):
            res += str(mat[i][left])+"  "
        left += 1

    print(res)



def SpiralMatrixTest():
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    spiralMatrix(mat)

SpiralMatrixTest()

