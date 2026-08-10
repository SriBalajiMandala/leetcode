class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        s=0
        n=len(nums)
        for i in range(n//2):
            s+=int(str(nums[i])+str(nums[n-1-i]))
        if len(nums)%2!=0:
            s+=nums[len(nums)//2]
        return s