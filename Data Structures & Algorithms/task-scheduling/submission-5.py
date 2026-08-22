class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxf = max(counts.values())
        idle = (maxf - 1) * n

        for _, freq in counts.items():
            idle -= min(maxf -1, freq)
        return max(0, idle + maxf - 1) + len(tasks)