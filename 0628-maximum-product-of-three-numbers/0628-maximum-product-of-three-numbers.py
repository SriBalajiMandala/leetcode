class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        l=sorted(nums)
        return max(l[-3]*l[-2]*l[-1],l[1]*l[0]*l[-1])