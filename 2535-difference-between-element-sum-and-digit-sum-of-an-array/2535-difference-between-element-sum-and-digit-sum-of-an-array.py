class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=sum(nums)
        d=0
        for i in nums:
            while i!=0:
                d+=i%10
                i//=10
        return s-d
            