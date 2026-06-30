class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0]*26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        count.sort()
        maxf = count[25]

        slot = maxf -1
        idle = slot * n

        for i in range(24, -1, -1):
            idle -= min(slot, count[i])
        return max(idle,0) + len(tasks)