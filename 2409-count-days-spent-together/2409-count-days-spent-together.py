class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31,28,31,30,31,30,
                  31,31,30,31,30,31]
        def days(date):
            m,d=map(int,date.split("-"))
            return sum(months[:m-1])+d
        a1=days(arriveAlice)
        print(a1)
        a2=days(leaveAlice)
        b1=days(arriveBob)
        b2=days(leaveBob)
        return max(0,min(a2,b2)-max(a1,b1)+1)