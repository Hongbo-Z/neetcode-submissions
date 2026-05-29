class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
            
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(cur, par):
            if cur in visit:
                return False
            visit.add(cur)

            for nei in adj[cur]:
                if nei == par:
                    continue
                if not dfs(nei, cur):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n

