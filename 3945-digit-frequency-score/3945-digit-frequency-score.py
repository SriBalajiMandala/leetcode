class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s=str(n)
        l=[]
        for i in (s):
            l.append(int(i))
        return (sum(l))