class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=n
        s=1
        o=0
        e=0
        while n!=0 and m!=0:
            if s%2==0:
                e+=s
                n-=1
            else:
                o+=s
                m-=1
            s+=1
        return abs(e-o)


                
        