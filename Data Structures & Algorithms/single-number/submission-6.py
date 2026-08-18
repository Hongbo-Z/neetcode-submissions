class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # res = 0
        # for num in nums:
        #     res ^= num
        # return res

        # 0 ^ N = N
        # N ^ N = 0

        # HashSet
        visit = set()
        for num in nums:
            if num in visit:
                visit.remove(num)
            else:
                visit.add(num)
        return visit.pop()
        