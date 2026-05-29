class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts = Counter(nums)
        # return [key for key, _ in counts.most_common(k)]

        counts = Counter(nums)
        arr = []
        for num, freq in counts.items():
            arr.append([freq, num])
        arr.sort(key = lambda x : x[0])

        output = [] 
        while len(output) < k:
            output.append(arr.pop()[1])
        return output


        