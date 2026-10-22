class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # n=len(nums)
        # ans=[1]*n
        # pre=1
        # for i in range(n):
        #     ans[i]=pre
        #     pre*=nums[i]
        # suf=1
        # for i in range(n-1,-1,-1):
        #     ans[i]*=suf
        #     suf*=nums[i]
        # return ans



        n=len(nums)
        if 0 in nums:
            result=[0]*n
            if nums.count(0)==1:
                zi=nums.index(0)
                nums.remove(0)
                result[zi]=math.prod(nums)
            return result
        tp=math.prod(nums)
        return [tp//i for i in nums]