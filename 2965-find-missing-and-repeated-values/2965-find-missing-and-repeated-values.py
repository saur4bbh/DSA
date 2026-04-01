class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        track = [0] * n*n
        ans = [0,0]

        for row in grid:
            for ele in row:
                if track[ele - 1] == 1:
                    ans[0] = ele
                else:
                    track[ele - 1] = 1
        
        for i in range(n*n):
            if track[i] == 0:
                ans[1] = i + 1
        
        return ans