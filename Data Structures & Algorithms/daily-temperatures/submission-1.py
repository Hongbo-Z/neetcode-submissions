class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [37, 36, 38]
        res = [0]*len(temperatures) 
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                i, t = stack.pop()
                res[i] = idx - i
            stack.append((idx, temp)) 
        return res
