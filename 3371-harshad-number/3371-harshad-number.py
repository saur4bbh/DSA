class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        copy = x
        val = 0
        while copy != 0:
            val += copy%10
            copy //= 10
        return val if x % val == 0 else -1