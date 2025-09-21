class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for money in accounts:
            wealth = max(wealth, sum(money))
        return wealth