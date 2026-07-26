class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l1=0
        l=len(arr)/4
        for i in arr:
            if arr.count(i)>=l:
                l1=i
        return l1
