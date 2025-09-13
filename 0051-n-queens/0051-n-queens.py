class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = []
        board = [['.'] * n for _ in range(n)]
        
        def check(r,c):
            for i in range(c):
                if board[r][i] == 'Q':
                    return False
                if r - (c - i) >= 0 and board[r - (c - i)][i] == 'Q':
                    return False
                if r + (c - i) < n and board[r + (c - i)][i] == 'Q':
                    return False
            return True
        
        def dfs(col):
            if col == n:
                ans.append([''.join(row) for row in board])
                return
            
            for row in range(n):
                
                if check(row, col):
                    board[row][col] = 'Q'
                    dfs(col+1)
                    board[row][col] = '.'
        
        dfs(0)
        return ans
                    