class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # l=[]
        # for i in range(len(prices)-2):
        #     v=abs(prices[i]-prices[i+1])
        #     l.append(v)
        # l.append(prices[-2])
        # l.append(prices[-1])
        # return l
        l=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    v=prices[i]-prices[j]
                    l.append(v)
                    break
            else:
                l.append(prices[i])
        return l