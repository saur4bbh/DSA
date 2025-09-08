class Solution:
    def countDigits(self, num: int) -> int:
        n = num
        count = 0

        while n != 0:
            if num % (n%10) == 0:
                count += 1
            n //= 10

        return count
