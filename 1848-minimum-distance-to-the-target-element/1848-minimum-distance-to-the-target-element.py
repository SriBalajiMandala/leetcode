class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        # l=[]
        # for i in nums:
        #     l.append(nums.index(target))
        # s=min(l)
        # return abs(s-start)
        res = len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                res = min(res, abs(i - start))
        return res
        