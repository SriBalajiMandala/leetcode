class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mi=min(nums)
        ma=max(nums)
        y=[]
        for i in range(1,ma+1):
            if mi%i==0 and ma%i==0:
                y.append(i)
        return max(y)
                
        
