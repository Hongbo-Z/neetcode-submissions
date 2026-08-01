class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = collections.defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        cycle = set()
        order = []

        def dfs(crs):
            if crs in cycle:
                return False
            
            if preMap[crs] == None: # if fully processed
                return True

            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            order.append(crs)
            preMap[crs] = None # mark this node as completed
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return order            
