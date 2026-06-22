class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                i, t = stack.pop()
                res[i] = idx - i
            else:
                stack.append([idx, temp])
        return res