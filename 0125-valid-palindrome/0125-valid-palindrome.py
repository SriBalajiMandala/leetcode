class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(' ','').lower()
        for i in s:
            if not i.isalnum():
                s=s.replace(i,'')
        return s==s[::-1]
            
            