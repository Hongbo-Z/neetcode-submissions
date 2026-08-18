class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rowZero, colZero = False, False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
                    if c > 0:
                        matrix[0][c] = 0
                    else:
                        colZero = True


        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if rowZero:
            matrix[0] = [0] * cols
        
        if colZero:
            for r in range(rows):
                matrix[r][0] = 0
        