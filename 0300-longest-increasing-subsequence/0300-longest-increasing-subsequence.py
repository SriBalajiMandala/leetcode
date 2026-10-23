class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        l=[1]*len(nums)
        res=1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    if l[j]+1>l[i]:
                        l[i]=l[j]+1
            res=max(res,l[i])
        return res