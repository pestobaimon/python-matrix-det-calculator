import copy

mat = [[1,2,3],
      [4,5,6],
      [7,8,9]]
for i in range(2):
    pivotedMat = copy.deepcopy(mat)
    for row in pivotedMat:
        del row[i]
    del pivotedMat[0]
    print(pivotedMat)