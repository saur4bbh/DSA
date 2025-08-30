class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def largest(cap):
            count = 1
            summ = 0
            for n in nums:
                summ += n
                if summ > cap:
                    count += 1
                    summ = n
            return count

        l, r = max(nums), sum(nums)

        while l <= r:
            mid = (l + r) // 2
            if largest(mid) <= k:
                r = mid - 1
            else:
                l = mid + 1
        
        return l
