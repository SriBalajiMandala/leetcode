class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < mi:
                mi = prices[i]
            else:
                profit = max(profit, prices[i] - mi)
        return profit


        # m=prices[0]
        # ma=0
        # for i in prices:
        #     if i<m:
        #         m=i
        #     p=i-m
        #     # print(m)
        #     if p>ma:
        #         ma=p
        # return ma