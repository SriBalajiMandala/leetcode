class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        s1=s2=s3=''
        for i in firstWord:
            s1+=str(ord(i)-97)
        for i in secondWord:
            s2+=str(ord(i)-97)
        for i in targetWord:
            s3+=str(ord(i)-97)
        return (int(s1)+int(s2))==int(s3)