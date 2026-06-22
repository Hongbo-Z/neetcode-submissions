class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        res = 0
        slow_time = 0
        for p, s in cars:
            if (target - p) / s > slow_time:
                slow_time = (target - p) / s 
                res += 1
        return res
        
            