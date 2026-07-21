class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l=[]
        if not nums: return 0
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d.keys():
            if d[i]==1:
                l.append(i)
        return l