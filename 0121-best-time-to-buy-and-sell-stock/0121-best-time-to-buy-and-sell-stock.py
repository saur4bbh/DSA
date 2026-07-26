class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 10**4
        profit = 0
        for p in prices:
            if p < low:
                low = p
            profit = max(p - low, profit)

        return profit