class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        if len(s)<=2:
            return 0
        
        def beauty(l,r):
            d = [0]*27
            for i in range(l,r+1):
                d[ord(s[i]) - ord('a')] += 1

            big, small = 0, 1000
            for i in d:
                if i > 0:
                    small = min(small, i)
                    big = max(big, i)
            return big - small
        
        count = 0
        for i in range(n-2):
            for j in range(i+2,n):
                count += beauty(i,j)

        return count
