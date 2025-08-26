class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)-1

        ans = len(nums)
        while l<=r:
            mid = (l+r)//2

            if target <= nums[mid]:
                ans = mid
                r = mid-1
            else:
                l = mid+1

        return ans