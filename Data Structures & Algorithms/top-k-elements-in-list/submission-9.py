class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        arr = []
        for num, freq in counts.items():
            arr.append([num, freq])
        arr.sort(key = lambda x:x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(arr[i][0])
        return res 