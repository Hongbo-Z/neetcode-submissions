class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        def dfs(leftPar, rightPar):
            if leftPar == rightPar == n:
                res.append("".join(subset))
            
            if leftPar < n:
                subset.append('(')
                dfs(leftPar+1, rightPar)
                subset.pop()
            if rightPar < leftPar:
                subset.append(')')
                dfs(leftPar, rightPar+1)
                subset.pop()
        dfs(0, 0)
        return res