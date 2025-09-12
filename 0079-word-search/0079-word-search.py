class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        visited = set()

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            
            if not (0 <= c < col) or not (0 <= r < row) or (r,c) in visited or board[r][c] != word[idx]:
                return False

            visited.add((r,c))
            res = dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1)
            visited.remove((r,c))

            return res
            

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        return False