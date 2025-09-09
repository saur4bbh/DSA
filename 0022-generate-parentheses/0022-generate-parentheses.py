class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        temp = []

        def backtrack(open, close):
            if open == 0 and close == 0:
                ans.append(''.join(temp))
                return

            if open != 0:
                temp.append('(')
                backtrack(open-1, close)
                temp.pop()

            if open < close and close != 0:
                temp.append(')')
                backtrack(open, close-1)
                temp.pop()
            
        backtrack(n, n)
        return ans