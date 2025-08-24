class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sn = n * (n+1) // 2
        s2n = n * (n+1) * (2 * n + 1) // 6

        s = s2 = 0
        for i in nums:
            s += i
            s2 += i * i

        val1 = sn - s                 #x-y
        val2 = (s2n - s2)//val1       #x^2 - y^2

        y = (val1 + val2)//2          #x+y
        x = y - val1
        
        return [x, y]