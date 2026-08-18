class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, left = 0, 0
        bottom, right = len(matrix), len(matrix[0])
        res = []

        while top < bottom and left < right:
            
            # Moving from left to right
            for j in range(left, right):
                res.append(matrix[top][j])
            top += 1

            # Moving from top to bottom
            for i in range(top, bottom):
                res.append(matrix[i][right -1])
            right -= 1

            if top == bottom or left == right:
                break
            
            # Moving from right to left
            for j in range(right-1, left - 1, -1):
                res.append(matrix[bottom-1][j])
            bottom -= 1

            # Moving from bottom to top
            for i in range(bottom-1, top -1, -1):
                res.append(matrix[i][left])
            left += 1
        return res