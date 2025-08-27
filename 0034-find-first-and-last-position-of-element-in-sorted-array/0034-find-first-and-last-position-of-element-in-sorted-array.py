class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        ansleft = -1

        while l<=r:
            mid = (l+r) // 2
            if nums[mid] >= target:
                r = mid - 1
                if nums[mid] == target:
                    ansleft = mid
            else:
                l = mid + 1
        
        l, r = 0, len(nums)-1
        ansright = -1

        while l<=r:
            mid = (l+r) // 2
            if nums[mid] <= target:
                l = mid + 1
                if nums[mid] == target:
                    ansright = mid
            else:
                r = mid - 1
        
        return [ansleft,ansright]