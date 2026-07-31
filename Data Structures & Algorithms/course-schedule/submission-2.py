class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        curToPre = collections.defaultdict(list)
        for cur, pre in prerequisites:
            curToPre[cur].append(pre)
        
        seen = set()
        def dfs(curr): # cycle detection
            if curr in seen:
                return False
            if curToPre[curr] == []:
                return True
            
            seen.add(curr)
            for pre in curToPre[curr]:
                if not dfs(pre):
                    return False
            seen.remove(curr)
            curToPre[curr] = []
            return True
        
        for num in range(numCourses):
            if not dfs(num):
                return False
        return True