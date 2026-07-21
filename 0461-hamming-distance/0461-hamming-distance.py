class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #return int(bin(x)[2:] or bin(y)[2:])
        d=x^y
        c=bin(d)[2:]
        s=0
        for i in range(len(c)):
            if c[i]=="1":
                s+=1
        return s