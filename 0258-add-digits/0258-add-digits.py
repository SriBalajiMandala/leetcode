class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # while num>=10:
        #     s=0
        #     d=0
        #     while num>0:
        #         d=num%10
        #         s+=d
        #         num//=10
        #     num=s
        # return num
        while num>=10:
            s=0
            for i in str(num):
                s+=int(i)
                num=s
        return num 