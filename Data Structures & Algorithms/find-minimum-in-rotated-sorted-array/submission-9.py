class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Low bound trick
        l, r = 0, len(nums) -1
        while l < r:
            mid = (l + r) //2
            if nums[mid] <= nums[r]: #  minimum could be mid or somewhere to its left
                r = mid
            else:
                l = mid + 1 # minimum must be to the right of mid
        return nums[l] # # At the end of that loop, l == r, and that index points to the minimum element.