class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Since nums is sorted, if nums[i] > 0,
            # then nums[i] + nums[l] + nums[r] must be > 0
            if nums[i] > 0:
                break

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate second number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate third number
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res
