class Solution:
    def addDigits(self, num: int) -> int:
        n = 0

        while True:
            while num != 0:
                n += num%10
                num //= 10

            if n // 10 == 0:
                return n
            num = n
            n = 0