class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=5:
            return False
        s=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                s+=i
                if i*i!=num:
                    s+=num//i
        if s==num:
            return True
        else:
            return False