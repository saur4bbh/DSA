class Solution:
    def pivotInteger(self, n: int) -> int:
        summ = n * (n+1) // 2
        x = int(summ ** 0.5)
        return x if x * x == summ else -1
        