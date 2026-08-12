class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # s=set()
        # for i in nums:
        #     if i in s:
        #         return True
        #     s.add(i)
        # return False
        s=set(nums)
        if len(nums)!=len(s):
            return True
        return False