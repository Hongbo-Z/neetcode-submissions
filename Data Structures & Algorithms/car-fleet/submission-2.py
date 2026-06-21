class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        fleets = 0
        slow_time = 0
        for p, s in cars:
            time = (target - p)/s
            if time > slow_time:
                fleets += 1
                slow_time = time
        return fleets 
