class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = []
        board = [['.'] * n for _ in range(n)]
        
        t_row = [False] * n
        t_1diag = [False] * (n+n-1)
        t_2diag = [False] * (n+n-1)
        
        def dfs(col):
            if col == n:
                ans.append([''.join(row) for row in board])
                return
            
            for row in range(n):
                if not t_row[row] and not t_1diag[row+col] and not t_2diag[n-1 + row-col]:
                    t_row[row] = t_1diag[row+col] = t_2diag[n-1 + row-col] = True

                    board[row][col] = 'Q'
                    dfs(col+1)
                    board[row][col] = '.'

                    t_row[row] = t_1diag[row+col] = t_2diag[n-1 + row-col] = False

        dfs(0)
        return ans
                    