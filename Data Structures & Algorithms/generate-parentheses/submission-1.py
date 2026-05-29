class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subSet = []
        def dfs(leftPar, rightPar):
            
            if leftPar == rightPar == n:
                res.append(''.join(subSet))
                return
            if leftPar < n:
                subSet.append('(')
                dfs(leftPar + 1, rightPar)
                subSet.pop()
            if rightPar < leftPar:
                subSet.append(')')
                dfs(leftPar, rightPar + 1)
                subSet.pop()
        dfs(0, 0)
        return res
        