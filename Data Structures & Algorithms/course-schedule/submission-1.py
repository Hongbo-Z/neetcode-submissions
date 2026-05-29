class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = collections.defaultdict(list)
        for cur, pre in prerequisites:
            preMap[cur].append(pre)
        
        visit = set()
        def dfs(cur) -> bool:
            if cur in visit:
                return False
            if preMap[cur] == []:
                return True

            visit.add(cur)
            for pre in preMap[cur]:
                if not dfs(pre):
                    return False
            visit.remove(cur)
            preMap[cur] = []
            return True

        for cur in range(numCourses):
            if not dfs(cur):
                return False
        return True