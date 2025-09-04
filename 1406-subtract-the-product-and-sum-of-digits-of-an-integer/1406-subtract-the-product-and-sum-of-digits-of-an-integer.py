class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        summ = 0
        while n != 0:
            x = n%10
            prod *= x
            summ += x
            n //= 10
        
        return prod - summ