class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            
            #right
            if c < col-1 and board[r][c + 1] == word[idx]: 
                temp = board[r][c]
                board[r][c] = None
                if dfs(r, c + 1, idx + 1):
                    return True
                board[r][c] = temp

            #left
            if c > 0 and board[r][c - 1] == word[idx]:
                temp = board[r][c]
                board[r][c] = None
                if dfs(r, c - 1, idx + 1):
                    return True
                board[r][c] = temp

            #down
            if r < row-1 and board[r + 1][c] == word[idx]:
                temp = board[r][c]
                board[r][c] = None
                if dfs(r + 1, c, idx + 1):
                    return True
                board[r][c] = temp

            #up
            if r > 0 and board[r - 1][c] == word[idx]:
                temp = board[r][c]
                board[r][c] = None
                if dfs(r - 1, c, idx + 1):
                    return True
                board[r][c] = temp


        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True
        return False