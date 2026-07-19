class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=[]
        a=0
        for i in gain:
            a+=i 
            n.append(a)
        if max(n)<0:
            return 0
        else:
            return max(n)