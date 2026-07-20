class Solution:
    def bitwiseComplement(self, n: int) -> int:
        l=bin(n)[2:]
        compliment=""
        for i in l:
            if i=="0":
                compliment+="1"
            else:
                compliment+="0"
        return int(compliment,2)