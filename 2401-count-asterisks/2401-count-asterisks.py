class Solution:
    def countAsterisks(self, s: str) -> int:
        switch = False
        cnt = 0
        for i in s:
            if not switch and i == '*':
                cnt += 1
            elif switch and i == '|':
                switch = False
            elif not switch and i == '|':
                switch = True
        return cnt