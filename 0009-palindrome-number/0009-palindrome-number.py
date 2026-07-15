class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """ 
        s=str(x)
        if x<0:
            s=s[1:]
        p=int(s[::-1])
        # r=int(p)
        if x==p:
            return True
        else:
            return False