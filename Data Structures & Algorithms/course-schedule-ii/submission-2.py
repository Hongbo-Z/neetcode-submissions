class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = collections.defaultdict(list)
        for curr, pre in prerequisites:
            preMap[curr].append(pre)
        
        order = []
        visit = set()

        def dfs(curr):
            if curr in visit:
                return False
            if preMap[curr] == None:
                return True
            
            visit.add(curr)
            for pre in preMap[curr]:
                if not dfs(pre):
                    return False
            visit.remove(curr)
            order.append(curr)
            preMap[curr] = None
            return True
            
        for cor in range(numCourses):
            if not dfs(cor):
                return []
        return order