class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # mi=min(prices)
        # print(mi)
        # s=prices[prices.index(mi):]
        # print(s)
        # ma=max(s)
        # return ma-mi
        m=prices[0]
        ma=0
        for i in prices:
            if i<m:
                m=i
            p=i-m
            if p>ma:
                ma=p
        return ma