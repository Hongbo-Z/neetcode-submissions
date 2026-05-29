class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute force
        # speed = 1
        # while speed <= max(piles):
        #     time = 0
        #     for pile in piles:
        #         time += math.ceil(pile/speed)
        #     if time <= h:
        #         return speed
        #     speed += 1

        # Bianry search
        l, r = 1, max(piles)
        res = r
        while l <= r:
            time = 0
            k = (l+r)//2
            for pile in piles:
                time += math.ceil(pile/k)
            if time <= h:
                res = k
                r = k - 1
            else:
                l = k +1
        return res
            
            




        