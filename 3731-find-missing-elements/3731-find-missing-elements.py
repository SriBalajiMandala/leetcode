class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l=[]
        ma=max(nums)
        mi=min(nums)
        for i in range(mi,ma):
            if i not in nums:
                l.append(i)
        return l