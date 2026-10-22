class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ma=0
        # for i in range(len(s)):
        #     seen=set()
        #     for j in range(i,len(s)):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #         ma=max(ma,j-i+1)
        # return ma

        seen=set()
        left=0
        res=0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            res=max(res,i-left+1)
        return res