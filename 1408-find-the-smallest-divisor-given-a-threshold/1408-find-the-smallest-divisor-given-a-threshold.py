class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)

        while l <= r:
            mid = (l + r) // 2
            val = sum( (i + mid - 1) // mid for i in nums)

            if val <= threshold:
                r = mid - 1
            else:
                l = mid + 1
            
        return l