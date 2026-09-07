class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for char in tasks:
            count[ord(char) - ord("A")] += 1
        
        count.sort(reverse = True)
        maxf = count[0]
        slot = maxf - 1
        idle = slot * n
        for i in range(1, 26):
            idle -= min(maxf - 1, count[i])
        return max(0, idle) + len(tasks)
