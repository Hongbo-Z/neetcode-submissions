class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(s):
                res.append(subset.copy())
                return
            
            for j in range(i, len(s)):
                if isPalin(s[i:j+1]):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop()

        def isPalin(string):
            return string == string[::-1]

        dfs(0)
        return res