class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0]*26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        count.sort(reverse = True)
        maxf = count[0]
        idle = (maxf - 1)*n
        for i in range(1, 26):
            idle -= min(maxf - 1, count[i])
        return max(0, idle) + len(tasks)

