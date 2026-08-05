class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]

        # Two poiters
        l, r = 0, len(numbers) -1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -=1
            else:
                return [l+1, r+1]
            
            
