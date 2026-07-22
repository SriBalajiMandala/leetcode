class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        l=0
        for i in nums:
            if nums.count(i)==1:
                l+=i
        return l