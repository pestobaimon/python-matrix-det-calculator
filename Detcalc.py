import copy
def calculateDet(mat):
    ans=0
    for row in mat:
        if(len(mat)!=len(row)):
            return 'err not square matrix'
    if len(mat) == 2:
        return mat[0][0]*mat[1][1] - mat[1][0]*mat[0][1]
    else:
        for i in range(len(mat)):
            pivotedMat = copy.deepcopy(mat)
            del pivotedMat[0]
            for row in pivotedMat:
                del row[i]
            ans+= mat[0][i]*calculateDet(pivotedMat)*pow(-1,i)
        return ans


mat = [[1,2,3,1,1],
      [4,21,6,4,1],
      [7,8,9,1,1],
      [9,9,6,1,3],
      [2,3,3,3,16]]

print(calculateDet(mat))