class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # d = collections.defaultdict(int)
        # for i in range(len(numbers)):
        #     if target - numbers[i] in d:
        #         return[d[target - numbers[i]], i+1]
        #     d[numbers[i]] = i + 1 

        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return []