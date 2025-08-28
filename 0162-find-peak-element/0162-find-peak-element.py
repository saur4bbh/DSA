class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[r] > nums[r-1]:
            return r


        while l<r:
            mid = (l+r)//2

            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            
            elif nums[mid] > nums[mid - 1]:
                    l = mid + 1
            else:
                    r = mid

        return l
  