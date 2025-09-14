class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [[set() for _ in range(3)] for __ in range(3)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':

                    row[r].add(val)
                    col[c].add(val)
                    box[r // 3][c // 3].add(val)

        
        def check(r, c, val):
            if val in row[r]:
                return False
            if val in col[c]:
                return False
            if val in box[r // 3][c // 3]:
                return False
            return True
        
        def backtrack(n):
            
            if n == 81:
                return True

            r = n // 9
            c = n % 9
            val = board[r][c]

            if val != '.':
                return backtrack(n+1)

            for i in range(1,10):
                curr = str(i)
                if check(r, c, curr):
                    row[r].add(curr)
                    col[c].add(curr)
                    box[r // 3][c // 3].add(curr)

                    board[r][c] = curr
                    if backtrack(n+1):
                        return True
                    board[r][c] = '.'

                    row[r].remove(curr)
                    col[c].remove(curr)
                    box[r // 3][c // 3].remove(curr)
            
            return False

        backtrack(0)
        return

            