class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # space optimized way O(1)
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False
        colZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if c > 0:
                        matrix[0][c] = 0
                    else:
                        colZero = True
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
        if colZero:
            for r in range(rows):
                matrix[r][0] = 0
        
          # Brute force
        # m, n = len(matrix), len(matrix[0])
        # rows, cols = set(), set() # use set to avoid duplicates
        # for i in range(m):
        #     for j in range(n):
        #         if not matrix[i][j]:
        #             rows.add(i)
        #             cols.add(j)
        # for r in rows:
        #     matrix[r] = [0]*m
        # for c in cols:
        #     for i in range(m):
        #         matrix[i][c] = 0

        
        