class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1} # prefixSum : counts
        curSum = 0
        res = 0
        for num in nums:
            curSum += num
            res += prefixSum.get(curSum - k, 0)
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        return res 