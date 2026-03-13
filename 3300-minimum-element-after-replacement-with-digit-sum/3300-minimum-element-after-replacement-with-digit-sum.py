class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = 10**5

        for num in nums:
            temp = 0

            while num > 0:
                temp += num%10
                num //= 10
            ans = min(ans, temp)
        
        return ans