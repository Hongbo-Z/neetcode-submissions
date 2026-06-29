class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zeroRow = False
        zeroCol = False

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i != 0:
                        matrix[i][0] = 0
                    else:
                        zeroRow = True

                    if j !=0:
                        matrix[0][j] = 0
                    else:
                        zeroCol = True

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if zeroRow:
            matrix[0] = [0]*cols
        if zeroCol:
            for i in range(rows):
                matrix[i][0] = 0
         
        