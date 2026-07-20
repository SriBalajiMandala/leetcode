class Solution:
    def bitwiseComplement(self, n: int) -> int:
        l=bin(n)[2:]
        comp=""
        for i in l:
            if i=="0":
                comp+="1"
            else:
                comp+="0"
        return int(comp,2)