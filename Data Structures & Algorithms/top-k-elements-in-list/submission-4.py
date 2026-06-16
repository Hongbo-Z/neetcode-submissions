class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        arr = []
        for num, freq in counts.items():
            arr.append([freq, num])
        arr.sort(key = lambda x: x[0])

        res = []

        for _ in range(k):
            res.append(arr.pop()[1])
        return res
            