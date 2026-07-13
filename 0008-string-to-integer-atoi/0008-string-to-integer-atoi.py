class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        tol=0
        sig=1
        if len(s)==0:
            return 0
        if s[0].isalpha() and s[0]!='+' and s[0]!='-':
            return 0
        elif s[0]=='-':
            sig=-1
            s=s[1:]
        elif s[0]=='+':
            s=s[1:]
        for i in s:
            if i.isdigit():
                tol=(tol*10)+int(i)
            else:
                break
        if tol*sig>2**31-1:
            return 2**31-1
        elif tol*sig<-2**31:
            return -2**31
        else:
            return tol*sig
        
        
        