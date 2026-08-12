class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in nums:
        #     if nums.count(i)>=2:
        #         return True
        # return False
        s=set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False