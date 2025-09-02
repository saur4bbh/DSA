class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)

        count = 0
        for i in range(n):
            d = [0]*26

            for j in range(i,n):
                d[ord(s[j]) - ord('a')] += 1

                small, big = 1000, 0
                for i in d:
                    if i > 0:
                        small = min(small, i)
                        big = max(big, i)

                count += big - small

        return count
