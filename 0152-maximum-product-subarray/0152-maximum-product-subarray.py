class Solution:
    def maxProduct(self, nums):
        res = float('-inf')
        maxi = mini = 1

        for n in nums:
            temp = maxi
            maxi = max(temp * n,mini * n, n)
            mini = min(temp * n,mini * n, n)

            res = max(maxi, res)

        return res