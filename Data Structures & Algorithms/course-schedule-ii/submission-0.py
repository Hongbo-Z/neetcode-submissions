class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for curr, pre in prerequisites:
            preMap[curr].append(pre)
        
        cycle = set() # Courses in the current DFS path
        visit = set()

        order = list()

        def dfs(curr)->bool: 
            if curr in cycle:
                return False
            if curr in visit:
                return True
            
            cycle.add(curr)
            for pre in preMap[curr]:
                if not dfs(pre):
                    return False
            cycle.remove(curr)
            visit.add(curr)
            order.append(curr)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return order