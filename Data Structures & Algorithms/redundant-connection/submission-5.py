class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)

        def dfs(node, par) -> bool:
            if node in visit:
                return True
            visit.add(node)

            for nei in adj[node]:
                # In an undirected graph, each edge is stored in both directions
                # This skips the node we just came from.
                if nei == par: 
                    continue
                    
                if dfs(nei, node):
                    return True
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = set()
            if dfs(u, -1):
                return [u, v]
        return []