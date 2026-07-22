class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if nums.count(i)==1:
                l.append(i)
        return sum(l)