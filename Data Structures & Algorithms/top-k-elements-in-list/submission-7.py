class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        
        arr = []
        for item, freq in count.items():
            arr.append([item, freq])
        arr.sort(key = lambda x: x[1])

        res = []
        for _ in range(k):
            res.append(arr.pop()[0])
        return res
