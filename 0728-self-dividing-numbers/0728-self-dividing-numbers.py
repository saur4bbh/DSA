class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def dividing(x):
            temp = x
            while temp != 0:
                num = temp % 10
                temp //= 10
                if num == 0 or x % num != 0:
                    return False
            return True
        
        ans = []
        for i in range(left, right+1):
            if dividing(i):
                ans.append(i)
        
        return ans