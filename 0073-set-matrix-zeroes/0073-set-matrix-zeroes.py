class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        lenc = len(matrix[0])
        lenr = len(matrix)
        col0 = False

        for r,row in enumerate(matrix):
            for c,ele in enumerate(row):
                if ele == 0:
                    if c == 0:
                        col0 = True
                    else: 
                        matrix[0][c] = 0
                    matrix[r][0] = 0

        for rr in range(1,lenr):
            for cc in range(1,lenc):
                if matrix[rr][0] == 0 or matrix[0][cc] == 0:
                    matrix[rr][cc] = 0
        
        if matrix[0][0] == 0:
            for c in range(1,lenc):
                matrix[0][c] = 0

        if col0:
            for r in range(lenr):
                matrix[r][0] = 0
