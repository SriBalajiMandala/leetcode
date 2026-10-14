class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        for i in nums:
            if i!=0:
                l.append(i)
        c=len(nums)-len(l)
        l.extend([0]*c)
        nums[:] = l
        return l
        