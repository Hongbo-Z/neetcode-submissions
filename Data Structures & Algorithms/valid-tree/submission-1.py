class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        def dfs(cur) -> None:
            if cur in seen:
                return
            seen.add(cur)

            for nei in graph[cur]:
                dfs(nei)
        dfs(0)
        return len(seen) == n