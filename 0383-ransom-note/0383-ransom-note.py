class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # for i in ransomNote:
        #     if i in magazine:
        #         return True
        #     else:
        #         return False
        # s=""
        # for i in range(len(ransomNote)):
        #     if ransomNote[i] in magazine:
        #         s+=ransomNote[i]
        #         magazine=magazine.replace(ransomNote[i],"",1)
        # if s==ransomNote:
        #     return True
        # else:
        #     return False
        for i in ransomNote:
            if i in magazine:
                magazine=magazine.replace(i,"",1)
            else:
                return False
        return True


