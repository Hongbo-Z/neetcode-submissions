class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        def dfs(node) -> None: # visit every node reachable from cur
            if node in seen:
                return
            seen.add(node)

            for nei in graph[node]:
                dfs(nei)
        dfs(0)
        return len(seen) == n