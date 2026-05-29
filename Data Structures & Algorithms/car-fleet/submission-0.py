class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        rank = [] # (position, time)
        for i in range(len(position)):
            rank.append((position[i],(target - position[i])/speed[i]))
        rank.sort(key = lambda x:x[0], reverse = True)

        stack = [rank[0]]
        
        for i in range(1,len(rank)):
            if rank[i][1] > stack[-1][1]:
                stack.append(rank[i])
        return len(stack)




