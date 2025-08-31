class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        def maxrow(idx):
            maxi = 0
            for j in range(n):
                if mat[j][idx] > mat[maxi][idx]:
                    maxi = j
            return maxi
        
        l, r = 0, m - 1
        while l <= r:

            j = (l + r) // 2
            i = maxrow(j)

            if (j == 0 or mat[i][j] > mat[i][j-1]) and (j == m-1 or mat[i][j] > mat[i][j+1]):
                return [i, j]
            elif mat[i][j+1] > mat[i][j]:
                l = j + 1
            else:
                r = j - 1
