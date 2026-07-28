class Solution:
    def maxScore(self, s: str) -> int:
        c=""
        l1=[]
        for i in range(len(s)-1):
            c+=s[i]
            x=c.count("0")
            r=s[i+1::]
            y=r.count("1")
            l1.append(x+y)
        return max(l1)