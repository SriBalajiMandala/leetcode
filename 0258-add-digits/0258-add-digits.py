class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>=10:
            s=0
            for i in str(num):
                s+=int(i)
                num=s
        return num 