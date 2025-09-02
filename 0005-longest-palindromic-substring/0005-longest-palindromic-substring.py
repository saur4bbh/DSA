class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def check(l,r):
            while 0<=l and r<=n-1 and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        start = end = 0

        for i in range(n):
            odd = check(i,i)
            even = check(i,i+1)
            maxi = max(odd, even)

            if maxi > end - start:
                start = i - (maxi - 1) // 2
                end = i + maxi // 2
    
        return s[start : end+1]
        