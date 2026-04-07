class Solution:
    def countEven(self, num: int) -> int:
        
        def evensum(x):
            temp = 0
            while x != 0:
                temp += x % 10
                x //= 10

            if temp % 2 == 0:
                return True
            else:
                return False
        
        ans = 0
        for i in range(1, num + 1):
            if evensum(i):
                ans += 1
        
        return ans