class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # two pointer
        # l, r = 0, 1
        # maxP = 0
        # while r <= len(prices) - 1:
        #     if prices[r] > prices[l]:
        #         maxP = max(maxP, prices[r] - prices[l])
        #     else:
        #         l = r
        #     r += 1
        # return maxP

        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)

        return maxP




            