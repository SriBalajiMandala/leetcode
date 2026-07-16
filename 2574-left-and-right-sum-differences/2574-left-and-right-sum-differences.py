class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        s=sum(nums)
        left=0
        l1=[]
        for i in nums:
            val=abs(left-(s-left-i))
            l1.append(val)
            left+=i        
        return l1