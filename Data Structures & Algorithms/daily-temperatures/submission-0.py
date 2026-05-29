class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [37, 36, 38]
        res = [0]*len(temperatures) 
        stack = []
        for idx, tem in enumerate(temperatures):
            while stack and tem > stack[-1][0]:
                t, i = stack.pop()
                res[i] = idx - i
            stack.append((tem, idx)) 
        return res
