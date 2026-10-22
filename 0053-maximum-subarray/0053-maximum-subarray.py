class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ma=nums[0]
        cu=nums[0]
        for i in range(1,len(nums)):
            cu=max(nums[i],cu+nums[i])
            ma=max(ma,cu)
        return ma