class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Method 1: Sorting. Time O(nlogn), Space O(n)
        # counts = Counter(nums)
        # arr = []
        # for num, freq in counts.items():
        #     arr.append([freq, num])
        # arr.sort(key = lambda x : x[0])

        # output = [] 
        # while len(output) < k:
        #     output.append(arr.pop()[1])
        # return output

        # Method 2: Bucket sort. Time O(n), Space O(n)
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        # The below operation avoid the use of sort()
        freqs = [[] for _ in range(len(nums)+1)]
        for num, freq in counts.items():
            freqs[freq].append(num)
        
        res = []
        for i in range(len(freqs)-1, 0, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res




        