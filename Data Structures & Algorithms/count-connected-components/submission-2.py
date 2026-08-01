class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            
            for nei in graph[node]:
                dfs(nei)

        res = 0
        for num in range(n):
            if num not in seen:
                res +=1
                dfs(num)
        return res