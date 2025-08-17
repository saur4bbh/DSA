class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        for i in range(len(prices)):
            cost = prices[i]-low
            if cost > profit: profit = cost
            if prices[i] < low: low = prices[i]
        return profit
