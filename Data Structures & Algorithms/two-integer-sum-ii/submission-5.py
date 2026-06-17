class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # Brute force of double loop
        # for l in range(len(numbers)):
        #     for r in range(l + 1, len(numbers)):
        #         if numbers[l] + numbers[r] == target:
        #             return [l+1, r+1]
                
        # return []

        # Two pointers

        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            if sum < target:
                l += 1
            if sum == target:
                return [l+1, r+1]

