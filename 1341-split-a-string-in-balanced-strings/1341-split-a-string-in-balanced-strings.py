class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        countR = 0
        countL = 0
        for i in s:
            if i == 'R':
                countR += 1
            else:
                countL += 1
            if countL == countR:
                ans += 1
        return ans