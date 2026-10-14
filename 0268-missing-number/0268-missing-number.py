class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ats=0
        exs=0
        n=len(nums)
        for i in nums:
            ats+=i
        exs=n*(n+1)/2
        return int(exs-ats)
