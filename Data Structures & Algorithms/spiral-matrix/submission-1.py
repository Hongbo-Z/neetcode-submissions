class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # [[1, 2, 3, 4], 
        #  [5, 6, 7, 8],
        #  [9,10, 11,12]]

        # Special cases
        # [[1,2,3,4]]

        #[[1],
        # [2],
        # [3]
        # [4]]
        top, left = 0, 0
        bottom, right = len(matrix), len(matrix[0])
        res = []
        
        while top < bottom and left < right:
            # moving from left to right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # moving from top to bottom
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            if not (top < bottom and left < right):
                break
            # moving from right to left
            for i in range(right -1, left - 1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            
            # moving from bottom to top
            for i in range(bottom -1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res


