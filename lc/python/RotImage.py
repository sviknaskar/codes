def transpose(mat):
    rows = len(mat)
    cols = len(mat[0])
    matT = [[0 for _ in range(rows)]for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            matT[j][i] = mat[i][j]

    mat = matT
    for i in range(cols):
        print(mat[i])


def rotateImage(mat):
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows):
        print(mat[i])

    for i in range(rows):
        for j in range(i, cols):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    print("#"*30)
    for i in range(rows):
        print(mat[i])

    for i in range(rows):
        mat[i] = mat[i][::-1]

    print("#" * 30)
    for i in range(rows):
        print(mat[i])


def rotateImageTest():
    mat = [
        [1,5,2],
        [5,7,3],
        [8,4,9]
    ]
    # rotateImage(mat)
    transpose(mat)

rotateImageTest()