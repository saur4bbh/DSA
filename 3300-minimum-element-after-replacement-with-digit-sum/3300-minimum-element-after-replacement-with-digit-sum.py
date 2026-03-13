class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = 10**5

        for i in range(len(nums)):
            temp = 0
            val = nums[i]

            while val > 0:
                temp += val%10
                val //= 10

            nums[i] = temp
            ans = min(ans, temp)
        
        return ans