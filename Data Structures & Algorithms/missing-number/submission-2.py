class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Method 1, Time: O(n^2) Space:O(1)
        # n = len(nums)
        # for i in range(n+1):
        #     if i in nums: # this take O(n) 
        #         continue
        #     else:
        #         return i

        # Method 2, Time: O(n) Space O(n)
        # nums_set = set(nums) # this need the extra space of O(n)
        # n = len(nums)
        # for i in range(n+1):
        #     if i not in nums_set: # hashmap is O(1)
        #         return i

        # Method 3
        n = len(nums)
        res = n
        for i in range(n):
            res ^= i ^ nums[i] # This equals res = res ^ i ^ nums[i]
        return res

        # Method 4
        # sum1, sum2 = 0, 0
        # n = len(nums)
        # for i in range(n+1):
        #     sum1 += i
        # for num in nums:
        #     sum2 += num
        # return sum1 - sum2





