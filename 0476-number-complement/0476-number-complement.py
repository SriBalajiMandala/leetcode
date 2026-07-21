class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num)[2:]
        st=""
        for i in b:
            if i=="0":
                st+="1"
            else:
                st+="0"
        return int(st,2)