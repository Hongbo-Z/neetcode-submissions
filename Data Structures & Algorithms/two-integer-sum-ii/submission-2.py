class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute force, Time O(n^2)
        # for i in range(len(numbers)):
        #     for j in range(i, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        # return []

        # Hash map, Space O(n)
        # d = collections.defaultdict(int)
        # for i in range(len(numbers)):
        #     if target - numbers[i] in d:
        #         return [d[target - numbers[i]], i+1]
        #     d[numbers[i]] = i+1
        # return []

        # Two pointer
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return[l+1, r+1]
            


