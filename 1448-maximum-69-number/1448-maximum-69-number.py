class Solution:
    def maximum69Number (self, num: int) -> int:
        tup = (1,10,100,1000)
        val = 0
        for i in tup:
            x = (num//i) %10
            if x == 6:
                val = 3 * i

        return num + val