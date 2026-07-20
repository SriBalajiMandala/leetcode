class Solution:
    def mirrorDistance(self, n: int) -> int:
        p=str(n)[::-1]
        return abs(int(p)-n)