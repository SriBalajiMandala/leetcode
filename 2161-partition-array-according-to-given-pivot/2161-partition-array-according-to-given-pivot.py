class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # ls=[]
        # gs=[]
        # e=[]
        # for i in nums:
        #     if i<pivot:
        #         ls.append(i)
        #     elif i==pivot:
        #         e.append(i)
        #     else:
        #         gs.append(i)
        # return ls+e+gs
        res=[]
        res=[i for i in nums if i<pivot]+[i for i in nums if i==pivot]+[i for i in nums if i>pivot]
        return res



