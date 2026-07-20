class Solution:
    def mirrorDistance(self, n: int) -> int:
        # p=str(n)[::-1]
        return abs(n-int(str(n)[::-1]))