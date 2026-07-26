class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        l=sorted(nums)
        a=l[-3]*l[-2]*l[-1]
        b=l[1]*l[0]*l[-1]
        return max(a,b)