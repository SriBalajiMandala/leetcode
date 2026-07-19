class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=[]
        a=0
        for i in gain:
            a+=i 
            n.append(a)
        return 0 if max(n)<0 else max(n)