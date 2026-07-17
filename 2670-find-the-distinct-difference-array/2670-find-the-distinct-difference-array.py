class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            p=len(set(nums[:i+1]))
            s=len(set(nums[i+1:]))
            re=p-s
            res.append(re)
        return res
            
