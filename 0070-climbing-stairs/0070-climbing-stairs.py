class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        f=1
        s=2
        for _ in range(3,n+1):
            t=f+s
            f=s
            s=t
        return s