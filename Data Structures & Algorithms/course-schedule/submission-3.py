class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = collections.defaultdict(list)
        for cur, pre in prerequisites:
            preMap[cur].append(pre)
        
        visit = set()
        def dfs(curr):
            if curr in visit:
                return False
            if preMap[curr] == []:
                return True

            visit.add(curr)
            for pre in preMap[curr]:
                if not dfs(pre):
                    return False
            visit.remove(curr)
            preMap[curr] = []

            return True
        
        for cor in range(numCourses):
            if not dfs(cor):
                return False
        return True