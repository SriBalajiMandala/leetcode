class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # l=set()
        # n2=set(nums2)
        # # for i in range(len(max(nums1,nums2))):.
        # for i in set(nums1):
        #     if i in n2:
        #         l.add(i)
        # if l:
        #     return min(l)
        # return -1/
        l=set(nums1).intersection(nums2)
        if l:
            return min(l)
        return -1