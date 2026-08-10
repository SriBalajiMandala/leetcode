class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # c=0
        # for i in grid:
        #     for j in i:
        #         if j<0:
        #             c+=1
        # return c
        count=0
        for li in grid:
            count+=len([i for i in li if i<0])
        return count 