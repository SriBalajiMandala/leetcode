class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return True if n%4==0 or n>=1 else False
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0