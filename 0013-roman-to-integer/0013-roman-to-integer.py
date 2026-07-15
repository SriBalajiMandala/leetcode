class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total=0
        pre=0
        val=0
        d={
            "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
        }
        for i in reversed(s):
            val=d[i]
            if val<pre:
                total-=val
            else:
                total+=val
                pre=val
        return total



        