class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        down = 0
        right = m - 1

        while down < n and right >= 0:
            val = matrix[down][right]

            if val == target:
                return True
            elif val > target:
                right -= 1
            else:
                down += 1
        
        return False