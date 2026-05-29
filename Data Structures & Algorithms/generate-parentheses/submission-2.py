class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # DSF Backtracking
        res = []
        stack = []
        def dfs(leftPar, rightPar):
            if leftPar == rightPar == n:
                res.append(''.join(stack))
                return None
            if leftPar < n:
                stack.append('(')
                dfs(leftPar + 1, rightPar)
                stack.pop()
            if rightPar < leftPar:
                stack.append(')')
                dfs(leftPar, rightPar + 1)
                stack.pop()
        dfs(0, 0)
        return res
        