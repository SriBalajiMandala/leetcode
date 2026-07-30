class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        i=0
        for _ in range(len(nums)//2):
            nums[i],nums[i+1]=nums[i+1],nums[i]
            i+=2
        return nums