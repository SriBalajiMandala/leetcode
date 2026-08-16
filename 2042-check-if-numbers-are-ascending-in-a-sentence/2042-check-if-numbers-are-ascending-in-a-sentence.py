class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # l=[]
        # for i in s.split():
        #     if i.isdigit():
        #         l.append(i)
        # print(l)
        # for i in range(1,len(l)):
        #     if l[i]>l[i-1]:
        #         return True
        #     else:
        #         return False
        c=0
        for i in s.split():
            if i.isdigit():
                m=int(i)
                if m>c:
                    c=m
                    continue
                else:
                    return False
        return True