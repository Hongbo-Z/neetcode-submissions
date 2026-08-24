class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        arr = []
        for num, freq in counts.items():
            arr.append([num, freq])
        arr.sort(key = lambda x:x[1])
        res = []
        for _ in range(k):
            res.append(arr.pop()[0])
        return res 