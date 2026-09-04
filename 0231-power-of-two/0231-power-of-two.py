class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if 2**n==0:
        #     return True
        # else:
        #     return False
        return n>0 and (n&(n-1)==0)