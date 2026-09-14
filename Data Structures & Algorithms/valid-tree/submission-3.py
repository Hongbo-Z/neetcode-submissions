class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1:
            return False
        
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in graph[node]:
                dfs(nei)
        dfs(0)
        return len(visit) == n