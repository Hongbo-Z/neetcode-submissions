class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        
        arr = []
        for item, freq in count.items():
            arr.append([item, freq])
        arr.sort(key = lambda x: x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(arr[i][0])
        return res
