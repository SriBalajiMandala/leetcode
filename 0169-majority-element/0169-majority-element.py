class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n=len(nums)/2
        # l=[]
        # for i in nums:
        #     if nums.count(i)>n:
        #         l.append(i)
        # return max(l)
        n=len(nums)/2
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i,j in d.items():
            if j>n:
                return i
