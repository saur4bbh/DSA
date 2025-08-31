class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        ans = []
        for r in range(len(mat)):
            maxi = 0
            for c in range(len(mat[0])):
                if mat[r][c] > mat[r][maxi]:
                    maxi = c
            
            x = True
            for r2 in range(len(mat)):
                if mat[r][maxi] < mat[r2][maxi]:
                    x = False
                    break
            
            if x == True:
                return [r,maxi]
