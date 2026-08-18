class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # st=""
        # for i in t:
        #     if i not in s:
        #         st+=i
        # return st
        t=list(t)
        for i in s:
            t.remove(i)
        return t[0]